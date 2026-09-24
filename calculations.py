import numpy as np
from scipy.stats import binom, hypergeom

# ============================================================
# 1. X-BAR CONTROL CHART
# ============================================================

def calculate_xbar(data):
    """
    Calculate X-Bar control chart statistics.

    Parameters
    ----------
    data : array-like
        Rows = samples
        Columns = observations inside each sample

    Returns
    -------
    dictionary containing:
        sample means
        sample ranges
        grand mean
        average range
        UCL
        LCL
        status
    """

    data = np.array(data, dtype=float)

    if data.ndim != 2:
        raise ValueError("Data must contain multiple samples.")

    n = data.shape[1]

    # d2 constants used for different sample sizes
    d2_values = {
        2: 1.128,
        3: 1.693,
        4: 2.059,
        5: 2.326,
        6: 2.534,
        7: 2.704,
        8: 2.847,
        9: 2.970,
        10: 3.078
    }

    if n not in d2_values:
        raise ValueError(
            "Sample size must currently be between 2 and 10."
        )

    d2 = d2_values[n]

    # Mean of every sample
    sample_means = np.mean(data, axis=1)

    # Range of every sample
    sample_ranges = (
        np.max(data, axis=1)
        - np.min(data, axis=1)
    )

    # Grand mean
    grand_mean = np.mean(sample_means)

    # Average range
    average_range = np.mean(sample_ranges)

    # Control limits
    ucl = (
        grand_mean
        + (3 * average_range)
        / (d2 * np.sqrt(n))
    )

    lcl = (
        grand_mean
        - (3 * average_range)
        / (d2 * np.sqrt(n))
    )

    # Detect points outside control limits
    out_of_control = np.where(
        (sample_means > ucl)
        | (sample_means < lcl)
    )[0]

    status = (
        "OUT OF CONTROL"
        if len(out_of_control) > 0
        else "IN CONTROL"
    )

    return {
        "sample_means": sample_means,
        "sample_ranges": sample_ranges,
        "grand_mean": grand_mean,
        "average_range": average_range,
        "ucl": ucl,
        "lcl": lcl,
        "out_of_control": out_of_control,
        "status": status
    }


# ============================================================
# 2. R CONTROL CHART
# ============================================================

def calculate_r_chart(data):
    """
    Calculate R-chart statistics.
    """

    data = np.array(data, dtype=float)

    if data.ndim != 2:
        raise ValueError("Data must contain multiple samples.")

    n = data.shape[1]

    constants = {
        2: (1.128, 0.853),
        3: (1.693, 0.888),
        4: (2.059, 0.880),
        5: (2.326, 0.864),
        6: (2.534, 0.848),
        7: (2.704, 0.833),
        8: (2.847, 0.820),
        9: (2.970, 0.808),
        10: (3.078, 0.797)
    }

    if n not in constants:
        raise ValueError(
            "Sample size must currently be between 2 and 10."
        )

    d2, d3 = constants[n]

    ranges = (
        np.max(data, axis=1)
        - np.min(data, axis=1)
    )

    r_bar = np.mean(ranges)

    # R-chart limits
    ucl = r_bar * (
        1 + (3 * d3 / d2)
    )

    lcl = r_bar * (
        1 - (3 * d3 / d2)
    )

    # Range cannot be negative
    lcl = max(0, lcl)

    out_of_control = np.where(
        (ranges > ucl)
        | (ranges < lcl)
    )[0]

    status = (
        "OUT OF CONTROL"
        if len(out_of_control) > 0
        else "IN CONTROL"
    )

    return {
        "ranges": ranges,
        "r_bar": r_bar,
        "ucl": ucl,
        "lcl": lcl,
        "out_of_control": out_of_control,
        "status": status
    }


# ============================================================
# 3. P CONTROL CHART
# ============================================================

def calculate_p_chart(proportions, sample_size):
    """
    Calculate p-chart statistics.

    proportions:
        Proportion of successful/correct/non-defective
        observations for each sample.

    sample_size:
        Number of observations per sample.
    """

    proportions = np.array(
        proportions,
        dtype=float
    )

    if np.any(proportions < 0) or np.any(proportions > 1):
        raise ValueError(
            "All proportions must be between 0 and 1."
        )

    if sample_size <= 0:
        raise ValueError(
            "Sample size must be greater than zero."
        )

    p_bar = np.mean(proportions)

    sigma_p = np.sqrt(
        (p_bar * (1 - p_bar))
        / sample_size
    )

    ucl = p_bar + (3 * sigma_p)
    lcl = p_bar - (3 * sigma_p)

    # Proportions cannot exceed 1 or fall below 0
    ucl = min(1, ucl)
    lcl = max(0, lcl)

    out_of_control = np.where(
        (proportions > ucl)
        | (proportions < lcl)
    )[0]

    status = (
        "OUT OF CONTROL"
        if len(out_of_control) > 0
        else "IN CONTROL"
    )

    return {
        "p_bar": p_bar,
        "ucl": ucl,
        "lcl": lcl,
        "out_of_control": out_of_control,
        "status": status
    }


# ============================================================
# 4. ACCEPTANCE SAMPLING
# ============================================================

def acceptance_sampling(
    lot_size,
    sample_size,
    defect_probability,
    acceptance_number,
    simulations=10000,
    seed=42
):
    """
    Acceptance sampling for a finite production lot.

    Calculates:
    1. Exact hypergeometric acceptance probability
    2. Binomial approximation
    3. Monte Carlo simulation
    """

    if lot_size <= 0:
        raise ValueError("Lot size must be greater than zero.")

    if sample_size <= 0:
        raise ValueError("Sample size must be greater than zero.")

    if sample_size > lot_size:
        raise ValueError(
            "Sample size cannot be greater than lot size."
        )

    if not 0 <= defect_probability <= 1:
        raise ValueError(
            "Defect probability must be between 0 and 1."
        )

    if acceptance_number < 0:
        raise ValueError(
            "Acceptance number cannot be negative."
        )

    # Convert defect rate into number of defective items
    defective_items = round(
        lot_size * defect_probability
    )

    # -----------------------------------------
    # 1. Exact finite-lot probability
    # Hypergeometric distribution
    # -----------------------------------------

    exact_probability = hypergeom.cdf(
        acceptance_number,
        lot_size,
        defective_items,
        sample_size
    )

    # -----------------------------------------
    # 2. Binomial approximation
    # -----------------------------------------

    binomial_probability = binom.cdf(
        acceptance_number,
        sample_size,
        defect_probability
    )

    # -----------------------------------------
    # 3. Monte Carlo simulation
    # -----------------------------------------

    rng = np.random.default_rng(seed)

    simulated_defects = rng.hypergeometric(
        ngood=lot_size - defective_items,
        nbad=defective_items,
        nsample=sample_size,
        size=simulations
    )

    simulated_probability = np.mean(
        simulated_defects <= acceptance_number
    )

    difference = abs(
        exact_probability -
        simulated_probability
    )

    return {
        "defective_items": defective_items,
        "exact_probability": exact_probability,
        "binomial_probability": binomial_probability,
        "simulated_probability": simulated_probability,
        "difference": difference,
        "simulated_defects": simulated_defects
    }