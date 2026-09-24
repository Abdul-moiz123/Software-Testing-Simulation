import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from calculations import (
    calculate_xbar,
    calculate_r_chart,
    calculate_p_chart,
    acceptance_sampling
)


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Quality Control Simulation",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Quality Control Simulation System")

st.write(
    """
    Simulation and verification of Quality Control techniques
    from Chapter 10 of *Statistics for Management, 8th Edition*.

    You can use the textbook examples, enter custom data,
    or upload your own CSV dataset.
    """
)

st.divider()


# ============================================================
# TEXTBOOK DATA
# ============================================================

TEXTBOOK_DATA = [
    [63, 55, 56, 53, 61, 64],
    [60, 63, 60, 65, 61, 66],
    [57, 60, 61, 65, 66, 62],
    [58, 64, 60, 61, 57, 65],
    [79, 68, 65, 61, 74, 71],

    [55, 66, 62, 63, 56, 52],
    [57, 61, 58, 64, 55, 63],
    [58, 51, 61, 57, 66, 59],
    [65, 66, 62, 68, 61, 67],
    [73, 66, 61, 70, 72, 78],

    [57, 63, 56, 64, 62, 59],
    [66, 63, 65, 59, 70, 61],
    [63, 53, 69, 60, 61, 58],
    [68, 67, 59, 58, 65, 59],
    [70, 62, 66, 80, 71, 76],

    [65, 59, 60, 61, 62, 65],
    [63, 69, 58, 56, 66, 61],
    [61, 56, 62, 59, 57, 55],
    [65, 57, 69, 62, 58, 72],
    [70, 60, 67, 79, 75, 68]
]


P_TEXTBOOK_DATA = [
    0.89, 0.91, 0.93, 0.95, 0.94,
    0.96, 0.92, 0.91, 0.93, 0.90,
    0.88, 0.94, 0.97, 0.94, 0.95,
    0.92, 0.93, 0.92, 0.91, 0.93,
    0.89
]


# ============================================================
# HELPER FUNCTION
# X-BAR / R DATA INPUT
# ============================================================

def get_variable_data():

    data_source = st.radio(
        "Choose Data Source",
        [
            "Chapter 10 Textbook Example",
            "Enter Custom Data",
            "Upload CSV"
        ]
    )

    # --------------------------------------------------------
    # TEXTBOOK
    # --------------------------------------------------------

    if data_source == "Chapter 10 Textbook Example":

        data = np.array(
            TEXTBOOK_DATA,
            dtype=float
        )

        st.success(
            "Using the Chapter 10 textbook example."
        )

        return data


    # --------------------------------------------------------
    # CUSTOM
    # --------------------------------------------------------

    elif data_source == "Enter Custom Data":

        st.write(
            """
            Enter one sample per line.

            Separate observations using commas.

            Example:
            """
        )

        st.code(
            """63,55,56,53,61,64
60,63,60,65,61,66
57,60,61,65,66,62"""
        )

        custom_text = st.text_area(
            "Enter Sample Data",
            height=220,
            placeholder=(
                "63,55,56,53,61,64\n"
                "60,63,60,65,61,66\n"
                "57,60,61,65,66,62"
            )
        )

        if not custom_text.strip():
            return None

        try:

            rows = []

            for line in custom_text.strip().splitlines():

                values = [
                    float(value.strip())
                    for value in line.split(",")
                ]

                rows.append(values)

            # All samples must have same size
            row_lengths = {
                len(row)
                for row in rows
            }

            if len(row_lengths) != 1:

                st.error(
                    "Every sample must contain the "
                    "same number of observations."
                )

                return None

            data = np.array(
                rows,
                dtype=float
            )

            return data

        except ValueError:

            st.error(
                "Invalid data. Use numbers separated "
                "by commas."
            )

            return None


    # --------------------------------------------------------
    # CSV
    # --------------------------------------------------------

    elif data_source == "Upload CSV":

        uploaded_file = st.file_uploader(
            "Upload CSV File",
            type=["csv"]
        )

        if uploaded_file is None:
            return None

        try:

            df = pd.read_csv(
                uploaded_file
            )

            st.write(
                "**Uploaded CSV Preview**"
            )

            st.dataframe(
                df.head(),
                use_container_width=True
            )

            # Keep numeric columns only
            numeric_df = df.select_dtypes(
                include=np.number
            )

            if numeric_df.empty:

                st.error(
                    "The CSV does not contain "
                    "numeric columns."
                )

                return None

            if numeric_df.shape[1] < 2:

                st.error(
                    "At least 2 numeric observation "
                    "columns are required."
                )

                return None

            st.info(
                f"""
                Detected **{numeric_df.shape[0]} samples**
                and **{numeric_df.shape[1]} numeric
                observations per sample**.
                """
            )

            return numeric_df.to_numpy(
                dtype=float
            )

        except Exception as e:

            st.error(
                f"Could not read CSV: {e}"
            )

            return None


# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.header(
    "Quality Control Methods"
)

analysis = st.sidebar.selectbox(
    "Select Analysis",
    [
        "X-Bar Control Chart",
        "R Control Chart",
        "p Control Chart",
        "Acceptance Sampling"
    ]
)


# ============================================================
# 1. X-BAR CONTROL CHART
# ============================================================

if analysis == "X-Bar Control Chart":

    st.header(
        "1. X-Bar Control Chart"
    )

    st.write(
        """
        The **X-Bar chart** monitors the average
        or mean of a process over time.
        """
    )

    st.subheader(
        "Step 1 — Select Data"
    )

    data = get_variable_data()

    if data is not None:

        # ----------------------------------------------------
        # VALIDATE SAMPLE SIZE
        # ----------------------------------------------------

        if data.shape[1] < 2:

            st.error(
                "Each sample must contain at least "
                "2 observations."
            )

        elif data.shape[1] > 10:

            st.error(
                """
                The current calculation engine supports
                sample sizes from 2 to 10 observations
                per sample.
                """
            )

        elif np.isnan(data).any():

            st.error(
                "The dataset contains missing values."
            )

        else:

            # ------------------------------------------------
            # DISPLAY DATA
            # ------------------------------------------------

            columns = [
                f"Observation {i + 1}"
                for i in range(
                    data.shape[1]
                )
            ]

            df = pd.DataFrame(
                data,
                columns=columns
            )

            df.index = np.arange(
                1,
                len(df) + 1
            )

            df.index.name = "Sample"

            st.subheader(
                "Step 2 — Review Data"
            )

            st.dataframe(
                df,
                use_container_width=True
            )

            col1, col2 = st.columns(2)

            col1.metric(
                "Number of Samples",
                data.shape[0]
            )

            col2.metric(
                "Observations per Sample",
                data.shape[1]
            )

            # ------------------------------------------------
            # RUN
            # ------------------------------------------------

            if st.button(
                "Run X-Bar Analysis",
                type="primary"
            ):

                try:

                    result = calculate_xbar(
                        data
                    )

                    st.subheader(
                        "Step 3 — Results"
                    )

                    col1, col2, col3, col4 = (
                        st.columns(4)
                    )

                    col1.metric(
                        "Grand Mean",
                        f"{result['grand_mean']:.2f}"
                    )

                    col2.metric(
                        "Average Range",
                        f"{result['average_range']:.2f}"
                    )

                    col3.metric(
                        "UCL",
                        f"{result['ucl']:.2f}"
                    )

                    col4.metric(
                        "LCL",
                        f"{result['lcl']:.2f}"
                    )

                    # ----------------------------------------
                    # STATUS
                    # ----------------------------------------

                    if (
                        result["status"]
                        == "IN CONTROL"
                    ):

                        st.success(
                            "Process Status: IN CONTROL"
                        )

                    else:

                        st.error(
                            "Process Status: OUT OF CONTROL"
                        )

                        samples = (
                            result[
                                "out_of_control"
                            ]
                            + 1
                        )

                        if len(samples) > 0:

                            st.write(
                                "**Samples outside limits:**",
                                ", ".join(
                                    map(
                                        str,
                                        samples
                                    )
                                )
                            )

                    # ----------------------------------------
                    # CALCULATION TABLE
                    # ----------------------------------------

                    results_df = pd.DataFrame({
                        "Sample":
                            np.arange(
                                1,
                                len(
                                    result[
                                        "sample_means"
                                    ]
                                ) + 1
                            ),

                        "Sample Mean":
                            result[
                                "sample_means"
                            ],

                        "Sample Range":
                            result[
                                "sample_ranges"
                            ]
                    })

                    st.subheader(
                        "Sample Calculations"
                    )

                    st.dataframe(
                        results_df.round(3),
                        use_container_width=True
                    )

                    # ----------------------------------------
                    # GRAPH
                    # ----------------------------------------

                    st.subheader(
                        "Step 4 — Control Chart"
                    )

                    fig, ax = plt.subplots(
                        figsize=(11, 5)
                    )

                    samples = np.arange(
                        1,
                        len(
                            result[
                                "sample_means"
                            ]
                        ) + 1
                    )

                    ax.plot(
                        samples,
                        result[
                            "sample_means"
                        ],
                        marker="o",
                        label="Sample Mean"
                    )

                    ax.axhline(
                        result[
                            "grand_mean"
                        ],
                        label=(
                            "Center Line "
                            f"({result['grand_mean']:.2f})"
                        )
                    )

                    ax.axhline(
                        result["ucl"],
                        linestyle="--",
                        label=(
                            f"UCL ({result['ucl']:.2f})"
                        )
                    )

                    ax.axhline(
                        result["lcl"],
                        linestyle="--",
                        label=(
                            f"LCL ({result['lcl']:.2f})"
                        )
                    )

                    ax.set_xlabel(
                        "Sample Number"
                    )

                    ax.set_ylabel(
                        "Sample Mean"
                    )

                    ax.set_title(
                        "X-Bar Control Chart"
                    )

                    ax.legend()

                    ax.grid(
                        True,
                        alpha=0.3
                    )

                    st.pyplot(fig)

                    plt.close(fig)

                    # ----------------------------------------
                    # VERIFICATION
                    # ----------------------------------------

                    st.subheader(
                        "Step 5 — Verification"
                    )

                    st.write(
                        """
                        The program calculated the sample
                        means, grand mean, average range,
                        upper control limit and lower
                        control limit automatically.

                        These results can be compared with
                        the manually solved numerical.
                        """
                    )

                except Exception as e:

                    st.error(
                        f"Calculation error: {e}"
                    )


# ============================================================
# 2. R CONTROL CHART
# ============================================================

elif analysis == "R Control Chart":

    st.header(
        "2. R Control Chart"
    )

    st.write(
        """
        The **R chart** monitors process variability.

        For each sample:

        **Range = Maximum Value − Minimum Value**
        """
    )

    st.subheader(
        "Step 1 — Select Data"
    )

    data = get_variable_data()

    if data is not None:

        if data.shape[1] < 2:

            st.error(
                "Each sample must contain at least "
                "2 observations."
            )

        elif data.shape[1] > 10:

            st.error(
                """
                The current calculation engine supports
                sample sizes from 2 to 10.
                """
            )

        elif np.isnan(data).any():

            st.error(
                "The dataset contains missing values."
            )

        else:

            columns = [
                f"Observation {i + 1}"
                for i in range(
                    data.shape[1]
                )
            ]

            df = pd.DataFrame(
                data,
                columns=columns
            )

            df.index = np.arange(
                1,
                len(df) + 1
            )

            df.index.name = "Sample"

            st.subheader(
                "Step 2 — Review Data"
            )

            st.dataframe(
                df,
                use_container_width=True
            )

            col1, col2 = st.columns(2)

            col1.metric(
                "Number of Samples",
                data.shape[0]
            )

            col2.metric(
                "Observations per Sample",
                data.shape[1]
            )

            if st.button(
                "Run R Chart Analysis",
                type="primary"
            ):

                try:

                    result = calculate_r_chart(
                        data
                    )

                    st.subheader(
                        "Step 3 — Results"
                    )

                    col1, col2, col3 = (
                        st.columns(3)
                    )

                    col1.metric(
                        "Average Range",
                        f"{result['r_bar']:.2f}"
                    )

                    col2.metric(
                        "UCL",
                        f"{result['ucl']:.2f}"
                    )

                    col3.metric(
                        "LCL",
                        f"{result['lcl']:.2f}"
                    )

                    if (
                        result["status"]
                        == "IN CONTROL"
                    ):

                        st.success(
                            "Process Status: IN CONTROL"
                        )

                    else:

                        st.error(
                            "Process Status: OUT OF CONTROL"
                        )

                        samples = (
                            result[
                                "out_of_control"
                            ]
                            + 1
                        )

                        if len(samples) > 0:

                            st.write(
                                "**Samples outside limits:**",
                                ", ".join(
                                    map(
                                        str,
                                        samples
                                    )
                                )
                            )

                    # ----------------------------------------
                    # TABLE
                    # ----------------------------------------

                    range_df = pd.DataFrame({
                        "Sample":
                            np.arange(
                                1,
                                len(
                                    result[
                                        "ranges"
                                    ]
                                ) + 1
                            ),

                        "Range":
                            result[
                                "ranges"
                            ]
                    })

                    st.subheader(
                        "Sample Range Calculations"
                    )

                    st.dataframe(
                        range_df.round(3),
                        use_container_width=True
                    )

                    # ----------------------------------------
                    # GRAPH
                    # ----------------------------------------

                    st.subheader(
                        "Step 4 — Control Chart"
                    )

                    fig, ax = plt.subplots(
                        figsize=(11, 5)
                    )

                    samples = np.arange(
                        1,
                        len(
                            result["ranges"]
                        ) + 1
                    )

                    ax.plot(
                        samples,
                        result["ranges"],
                        marker="o",
                        label="Sample Range"
                    )

                    ax.axhline(
                        result["r_bar"],
                        label=(
                            "R-Bar "
                            f"({result['r_bar']:.2f})"
                        )
                    )

                    ax.axhline(
                        result["ucl"],
                        linestyle="--",
                        label=(
                            f"UCL ({result['ucl']:.2f})"
                        )
                    )

                    ax.axhline(
                        result["lcl"],
                        linestyle="--",
                        label=(
                            f"LCL ({result['lcl']:.2f})"
                        )
                    )

                    ax.set_xlabel(
                        "Sample Number"
                    )

                    ax.set_ylabel(
                        "Range"
                    )

                    ax.set_title(
                        "R Control Chart"
                    )

                    ax.legend()

                    ax.grid(
                        True,
                        alpha=0.3
                    )

                    st.pyplot(fig)

                    plt.close(fig)

                    st.subheader(
                        "Step 5 — Interpretation"
                    )

                    st.write(
                        """
                        The R chart shows whether the
                        amount of variation in the process
                        remains statistically stable.
                        """
                    )

                except Exception as e:

                    st.error(
                        f"Calculation error: {e}"
                    )


# ============================================================
# 3. P CONTROL CHART
# ============================================================

elif analysis == "p Control Chart":

    st.header(
        "3. p Control Chart"
    )

    st.write(
        """
        The **p chart** monitors a proportion across
        multiple samples.

        Values must be between **0 and 1**.

        For example:

        **0.93 = 93%**
        """
    )

    st.subheader(
        "Step 1 — Select Data"
    )

    p_source = st.radio(
        "Choose Data Source",
        [
            "Chapter 10 Textbook Example",
            "Enter Custom Data",
            "Upload CSV"
        ]
    )

    proportions = None
    sample_size = None

    # --------------------------------------------------------
    # TEXTBOOK P DATA
    # --------------------------------------------------------

    if (
        p_source
        == "Chapter 10 Textbook Example"
    ):

        proportions = np.array(
            P_TEXTBOOK_DATA,
            dtype=float
        )

        sample_size = 200

        st.success(
            "Using the Chapter 10 example."
        )

        st.info(
            "Sample size per day = 200"
        )


    # --------------------------------------------------------
    # CUSTOM P DATA
    # --------------------------------------------------------

    elif (
        p_source
        == "Enter Custom Data"
    ):

        sample_size = st.number_input(
            "Sample Size Per Sample",
            min_value=1,
            value=200
        )

        st.write(
            """
            Enter proportions separated by commas.

            Example:
            """
        )

        st.code(
            "0.89,0.91,0.93,0.95,0.94"
        )

        custom_p = st.text_area(
            "Enter Proportions",
            placeholder=(
                "0.89,0.91,0.93,0.95,0.94"
            )
        )

        if custom_p.strip():

            try:

                proportions = np.array(
                    [
                        float(x.strip())
                        for x
                        in custom_p.split(",")
                    ],
                    dtype=float
                )

                if np.any(
                    proportions < 0
                ) or np.any(
                    proportions > 1
                ):

                    st.error(
                        "Every proportion must be "
                        "between 0 and 1."
                    )

                    proportions = None

            except ValueError:

                st.error(
                    "Enter valid numbers separated "
                    "by commas."
                )


    # --------------------------------------------------------
    # CSV P DATA
    # --------------------------------------------------------

    elif p_source == "Upload CSV":

        uploaded_p = st.file_uploader(
            "Upload p Chart CSV",
            type=["csv"]
        )

        if uploaded_p is not None:

            try:

                uploaded_df = pd.read_csv(
                    uploaded_p
                )

                st.subheader(
                    "Uploaded Data"
                )

                st.dataframe(
                    uploaded_df.head(),
                    use_container_width=True
                )

                numeric_columns = (
                    uploaded_df
                    .select_dtypes(
                        include=np.number
                    )
                    .columns
                    .tolist()
                )

                if not numeric_columns:

                    st.error(
                        "No numeric columns found."
                    )

                else:

                    selected_column = (
                        st.selectbox(
                            "Select Proportion Column",
                            numeric_columns
                        )
                    )

                    sample_size = (
                        st.number_input(
                            "Sample Size Per Sample",
                            min_value=1,
                            value=200
                        )
                    )

                    proportions = (
                        uploaded_df[
                            selected_column
                        ]
                        .dropna()
                        .to_numpy(
                            dtype=float
                        )
                    )

                    if np.any(
                        proportions < 0
                    ) or np.any(
                        proportions > 1
                    ):

                        st.error(
                            """
                            The selected column contains
                            values outside 0 to 1.
                            """
                        )

                        proportions = None

            except Exception as e:

                st.error(
                    f"Could not read CSV: {e}"
                )


    # --------------------------------------------------------
    # RUN P CHART
    # --------------------------------------------------------

    if proportions is not None:

        p_df = pd.DataFrame({
            "Sample":
                np.arange(
                    1,
                    len(proportions) + 1
                ),

            "Proportion":
                proportions,

            "Percentage":
                proportions * 100
        })

        st.subheader(
            "Step 2 — Review Data"
        )

        st.dataframe(
            p_df.round(4),
            use_container_width=True
        )

        if st.button(
            "Run p Chart Analysis",
            type="primary"
        ):

            try:

                result = calculate_p_chart(
                    proportions,
                    int(sample_size)
                )

                st.subheader(
                    "Step 3 — Results"
                )

                col1, col2, col3 = (
                    st.columns(3)
                )

                col1.metric(
                    "Average Proportion",
                    f"{result['p_bar']:.4f}"
                )

                col2.metric(
                    "UCL",
                    f"{result['ucl']:.4f}"
                )

                col3.metric(
                    "LCL",
                    f"{result['lcl']:.4f}"
                )

                if (
                    result["status"]
                    == "IN CONTROL"
                ):

                    st.success(
                        "Process Status: IN CONTROL"
                    )

                else:

                    st.error(
                        "Process Status: OUT OF CONTROL"
                    )

                    bad_samples = (
                        result[
                            "out_of_control"
                        ]
                        + 1
                    )

                    if len(
                        bad_samples
                    ) > 0:

                        st.write(
                            "**Samples outside limits:**",
                            ", ".join(
                                map(
                                    str,
                                    bad_samples
                                )
                            )
                        )

                # --------------------------------------------
                # GRAPH
                # --------------------------------------------

                st.subheader(
                    "Step 4 — Control Chart"
                )

                fig, ax = plt.subplots(
                    figsize=(11, 5)
                )

                samples = np.arange(
                    1,
                    len(proportions) + 1
                )

                ax.plot(
                    samples,
                    proportions,
                    marker="o",
                    label="Observed Proportion"
                )

                ax.axhline(
                    result["p_bar"],
                    label=(
                        "Center Line "
                        f"({result['p_bar']:.4f})"
                    )
                )

                ax.axhline(
                    result["ucl"],
                    linestyle="--",
                    label=(
                        f"UCL ({result['ucl']:.4f})"
                    )
                )

                ax.axhline(
                    result["lcl"],
                    linestyle="--",
                    label=(
                        f"LCL ({result['lcl']:.4f})"
                    )
                )

                ax.set_xlabel(
                    "Sample Number"
                )

                ax.set_ylabel(
                    "Proportion"
                )

                ax.set_title(
                    "p Control Chart"
                )

                ax.legend()

                ax.grid(
                    True,
                    alpha=0.3
                )

                st.pyplot(fig)

                plt.close(fig)

                st.subheader(
                    "Step 5 — Interpretation"
                )

                st.write(
                    """
                    Points outside the calculated
                    control limits indicate that the
                    process may contain special-cause
                    variation.
                    """
                )

            except Exception as e:

                st.error(
                    f"Calculation error: {e}"
                )


# ============================================================
# 4. ACCEPTANCE SAMPLING
# ============================================================

elif analysis == "Acceptance Sampling":

    st.header(
        "4. Acceptance Sampling"
    )

    st.write(
        """
        Acceptance sampling determines whether a
        production lot should be accepted or rejected
        by inspecting a sample from the lot.

        This module compares:

        - Exact Hypergeometric Probability
        - Binomial Approximation
        - Monte Carlo Simulation
        """
    )

    st.subheader(
        "Step 1 — Enter Sampling Plan"
    )

    col1, col2 = st.columns(2)

    with col1:

        lot_size = st.number_input(
            "Lot Size",
            min_value=1,
            value=1000,
            step=100
        )

        sample_size = st.number_input(
            "Sample Size",
            min_value=1,
            value=100,
            step=10
        )

        defect_probability = (
            st.number_input(
                "Defect Probability",
                min_value=0.0,
                max_value=1.0,
                value=0.01,
                step=0.001,
                format="%.3f"
            )
        )

    with col2:

        acceptance_number = (
            st.number_input(
                "Acceptance Number (c)",
                min_value=0,
                value=1,
                step=1
            )
        )

        simulations = st.number_input(
            "Monte Carlo Simulations",
            min_value=100,
            value=10000,
            step=1000
        )

    if sample_size > lot_size:

        st.error(
            "Sample size cannot be greater "
            "than lot size."
        )

    else:

        estimated_defective = round(
            lot_size
            * defect_probability
        )

        st.info(
            f"""
            **Sampling Plan**

            Lot Size: **{int(lot_size):,}**

            Defect Rate:
            **{defect_probability * 100:.2f}%**

            Defective Items:
            **{estimated_defective}**

            Sample Size:
            **{int(sample_size)}**

            Acceptance Number:
            **{int(acceptance_number)}**

            The lot is accepted if the sample
            contains **{int(acceptance_number)}
            or fewer defective items**.
            """
        )

        if st.button(
            "Run Acceptance Sampling",
            type="primary"
        ):

            try:

                result = acceptance_sampling(
                    lot_size=int(
                        lot_size
                    ),

                    sample_size=int(
                        sample_size
                    ),

                    defect_probability=float(
                        defect_probability
                    ),

                    acceptance_number=int(
                        acceptance_number
                    ),

                    simulations=int(
                        simulations
                    )
                )

                # --------------------------------------------
                # RESULTS
                # --------------------------------------------

                st.subheader(
                    "Step 2 — Results"
                )

                col1, col2, col3, col4 = (
                    st.columns(4)
                )

                col1.metric(
                    "Exact Hypergeometric",
                    (
                        f"{result['exact_probability'] * 100:.2f}%"
                    )
                )

                col2.metric(
                    "Binomial Approx.",
                    (
                        f"{result['binomial_probability'] * 100:.2f}%"
                    )
                )

                col3.metric(
                    "Monte Carlo",
                    (
                        f"{result['simulated_probability'] * 100:.2f}%"
                    )
                )

                col4.metric(
                    "Difference",
                    (
                        f"{result['difference'] * 100:.2f}%"
                    )
                )

                # --------------------------------------------
                # VERIFICATION
                # --------------------------------------------

                if (
                    result["difference"]
                    < 0.02
                ):

                    st.success(
                        """
                        VERIFIED: Monte Carlo simulation
                        closely agrees with the exact
                        finite-lot calculation.
                        """
                    )

                else:

                    st.warning(
                        """
                        Increase the number of simulations
                        for greater precision.
                        """
                    )

                # --------------------------------------------
                # TABLE
                # --------------------------------------------

                comparison = pd.DataFrame({
                    "Method": [
                        "Exact Hypergeometric",
                        "Binomial Approximation",
                        "Monte Carlo Simulation"
                    ],

                    "Probability": [
                        result[
                            "exact_probability"
                        ],

                        result[
                            "binomial_probability"
                        ],

                        result[
                            "simulated_probability"
                        ]
                    ]
                })

                comparison[
                    "Percentage"
                ] = (
                    comparison[
                        "Probability"
                    ]
                    * 100
                )

                st.subheader(
                    "Step 3 — Comparison"
                )

                st.dataframe(
                    comparison.round(4),
                    use_container_width=True
                )

                # --------------------------------------------
                # HISTOGRAM
                # --------------------------------------------

                st.subheader(
                    "Step 4 — Monte Carlo Simulation"
                )

                simulated_defects = (
                    result[
                        "simulated_defects"
                    ]
                )

                fig, ax = plt.subplots(
                    figsize=(11, 5)
                )

                bins = np.arange(
                    simulated_defects.max()
                    + 2
                ) - 0.5

                ax.hist(
                    simulated_defects,
                    bins=bins,
                    edgecolor="black"
                )

                ax.axvline(
                    acceptance_number
                    + 0.5,
                    linestyle="--",
                    linewidth=2,
                    label=(
                        "Acceptance / "
                        "Rejection Boundary"
                    )
                )

                ax.set_xlabel(
                    "Defective Items in Sample"
                )

                ax.set_ylabel(
                    "Frequency"
                )

                ax.set_title(
                    "Monte Carlo Acceptance "
                    "Sampling Simulation"
                )

                ax.legend()

                ax.grid(
                    True,
                    alpha=0.3
                )

                st.pyplot(fig)

                plt.close(fig)

                # --------------------------------------------
                # CONCLUSION
                # --------------------------------------------

                st.subheader(
                    "Step 5 — Verification Conclusion"
                )

                st.write(
                    f"""
                    The exact finite-lot calculation
                    produced an acceptance probability of
                    **{result['exact_probability'] * 100:.2f}%**.

                    The Monte Carlo simulation produced
                    approximately
                    **{result['simulated_probability'] * 100:.2f}%**.

                    The difference is
                    **{result['difference'] * 100:.2f}
                    percentage points**.

                    This comparison is used to verify the
                    theoretical acceptance-sampling
                    calculation.
                    """
                )

            except Exception as e:

                st.error(
                    f"Simulation error: {e}"
                )


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "Software Quality Engineering & Testing | "
    "Part 2B — Quality Control Numerical Verification "
    "and Simulation"
)