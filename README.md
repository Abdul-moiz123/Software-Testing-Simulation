# 📊 Quality Control Simulation System

A beginner-friendly web application for **simulating, calculating, visualizing, and verifying Statistical Quality Control techniques**.

The project was developed for **Software Quality Engineering & Testing — Part 2B**, where statistical simulation tools are used to verify manually solved Quality Control numericals.

The application is built with **Python and Streamlit** and covers four major Quality Control techniques:

1. X-Bar Control Chart
2. R Control Chart
3. p Control Chart
4. Acceptance Sampling

No previous knowledge of statistics, Python, or Quality Control is required to understand the basic purpose of this project.

---

# 📖 Table of Contents

* [What Is This Project?](#-what-is-this-project)
* [Why Was It Created?](#-why-was-it-created)
* [What Is Quality Control?](#-what-is-quality-control)
* [What Does Verification Mean?](#-what-does-verification-mean)
* [Features](#-features)
* [How the System Works](#-how-the-system-works)
* [1. X-Bar Control Chart](#1️⃣-x-bar-control-chart)
* [2. R Control Chart](#2️⃣-r-control-chart)
* [3. p Control Chart](#3️⃣-p-control-chart)
* [4. Acceptance Sampling](#4️⃣-acceptance-sampling)
* [Understanding Control Limits](#-understanding-control-limits)
* [Textbook vs Custom Data](#-textbook-vs-custom-data)
* [CSV Upload](#-csv-upload)
* [Project Structure](#-project-structure)
* [Technologies Used](#-technologies-used)
* [Installation](#-installation)
* [Running the Application](#-running-the-application)
* [Example Inputs](#-example-inputs)
* [Understanding the Results](#-understanding-the-results)
* [Acceptance Sampling Simulation](#-acceptance-sampling-simulation)
* [Reproducibility](#-reproducibility)
* [Limitations](#-limitations)
* [Educational Purpose](#-educational-purpose)
* [Future Improvements](#-future-improvements)
* [Author](#-author)

---

# 🎯 What Is This Project?

The **Quality Control Simulation System** is a web application that helps users understand and verify statistical Quality Control calculations.

Normally, students solve Quality Control problems manually using formulas.

For example:

```text
Given Data
    ↓
Calculate Sample Means
    ↓
Calculate Grand Mean
    ↓
Calculate Control Limits
    ↓
Draw Control Chart
    ↓
Decide Whether Process Is In Control
```

This application performs these calculations automatically.

It also creates graphs so that users can visually understand the results.

The basic workflow is:

```text
Manual/Textbook Numerical
          ↓
Enter Data into Application
          ↓
Python Performs Calculation
          ↓
Statistical Results Generated
          ↓
Graph Generated
          ↓
Compare Results
          ↓
Verification
```

If the software calculation agrees with the manually calculated result, the numerical has been computationally verified.

---

# 🎓 Why Was It Created?

This project was developed for:

**Software Quality Engineering & Testing**

Specifically:

**Part 2B — Use simulation tools to verify results of Quality Control numericals.**

The statistical concepts are based on topics from:

**Statistics for Management, 8th Edition**

Chapter 10:

**Quality and Quality Control**

Instead of only presenting handwritten calculations, this project demonstrates how the same Quality Control techniques can be implemented using software.

---

# 🏭 What Is Quality Control?

Quality Control is the process of checking whether a product, service, or process is operating at an acceptable and consistent level.

Consider a factory producing bottles.

The factory wants every bottle to contain approximately:

```text
500 ml
```

However, actual bottles may contain:

```text
498 ml
501 ml
500 ml
503 ml
497 ml
```

Some variation is normal.

The important question is:

> Is the variation normal, or has something unusual happened to the process?

Statistical Quality Control helps answer this question using data.

---

# 🔍 What Does Verification Mean?

Suppose a numerical is solved manually and gives:

```text
Grand Mean = 63.00
```

The same dataset is entered into this application.

If Python also calculates:

```text
Grand Mean = 63.00
```

the result has been computationally verified.

For simulation-based methods, such as Acceptance Sampling, the application can additionally compare theoretical probability with repeated simulated experiments.

---

# ✨ Features

The system currently provides:

* 📊 X-Bar Control Chart
* 📈 R Control Chart
* 📉 p Control Chart
* 🎲 Acceptance Sampling
* 🧮 Automatic statistical calculations
* 📋 Calculation tables
* 📈 Automatic graph generation
* 🚨 Out-of-control detection
* 📚 Built-in textbook examples
* ✍️ Custom data entry
* 📁 CSV file upload
* 🎲 Monte Carlo simulation
* 🔢 Exact probability calculation
* 🔬 Binomial approximation
* 📊 Hypergeometric distribution
* 🔄 Theoretical vs simulated result comparison
* 🌐 Interactive Streamlit interface

---

# ⚙️ How the System Works

The application contains four main analysis modules.

```text
Quality Control Simulation System
│
├── X-Bar Control Chart
│
├── R Control Chart
│
├── p Control Chart
│
└── Acceptance Sampling
```

Each method answers a different Quality Control question.

| Method              | Main Question                                                               |
| ------------------- | --------------------------------------------------------------------------- |
| X-Bar Chart         | Is the process average stable?                                              |
| R Chart             | Is process variability stable?                                              |
| p Chart             | Is the observed proportion stable?                                          |
| Acceptance Sampling | Should this production lot be accepted or rejected under the sampling plan? |

---

# 1️⃣ X-Bar Control Chart

## What is an X-Bar Chart?

An **X-Bar Control Chart** monitors the average value of a process.

Imagine measuring the time required to complete transactions.

Instead of looking at every transaction separately, several transactions are grouped into samples.

Example:

```text
Sample 1:
63, 55, 56, 53, 61, 64

Sample 2:
60, 63, 60, 65, 61, 66
```

The average of each sample is calculated.

For a sample containing:

```text
10, 12, 11, 13, 12
```

the sample mean is:

```text
(10 + 12 + 11 + 13 + 12) / 5

= 11.6
```

The same calculation is performed for every sample.

---

## Grand Mean

After calculating all sample means, the system calculates the **Grand Mean**.

The Grand Mean represents the overall process average.

Conceptually:

```text
Grand Mean
=
Average of all sample means
```

It becomes the center line of the X-Bar chart.

---

## Control Limits

The application calculates:

```text
UCL = Upper Control Limit

CL = Center Line

LCL = Lower Control Limit
```

The X-Bar control limits used by this implementation are based on the average-range method:

```text
UCL = X̄̄ + 3R̄ / (d₂√n)

LCL = X̄̄ - 3R̄ / (d₂√n)
```

Where:

```text
X̄̄ = Grand Mean

R̄ = Average Range

n = Number of observations in each sample

d₂ = Statistical constant based on sample size
```

---

## How to Interpret It

A simplified interpretation is:

```text
Point inside limits
        ↓
No point-level control-limit violation

Point outside limits
        ↓
Possible special-cause variation
```

The application automatically identifies sample means outside the calculated limits.

Important: a process can still require further investigation even when no individual point crosses a control limit. Full Statistical Process Control can also consider non-random patterns, runs, trends, and other rules.

---

# 2️⃣ R Control Chart

## What Is an R Chart?

The **R Control Chart** measures process variability.

While the X-Bar chart focuses on the process average, the R chart focuses on how spread out the observations are.

For every sample:

```text
Range = Maximum Value - Minimum Value
```

Example:

```text
Sample:

10, 12, 15, 11, 13

Maximum = 15
Minimum = 10

Range = 15 - 10

Range = 5
```

The range is calculated for every sample.

---

## Average Range

After calculating all ranges:

```text
R̄ = Average of all sample ranges
```

This becomes the center line of the R chart.

---

## Why Is the R Chart Important?

Imagine two processes.

### Process A

```text
49, 50, 51, 50, 50
```

### Process B

```text
30, 70, 40, 60, 50
```

Both may have similar averages.

However, Process B has much greater variation.

The R chart helps detect this difference.

---

## R Chart Limits

This project calculates R-chart limits using statistical constants based on subgroup size.

Conceptually:

```text
Upper Control Limit
        ↑

Observed Sample Ranges

Average Range
        ↓

Lower Control Limit
```

If a range falls outside the calculated limits, the application identifies the sample as potentially out of control.

---

# 3️⃣ p Control Chart

## What Is a p Chart?

A **p Control Chart** monitors proportions.

A proportion is a value between:

```text
0 and 1
```

For example:

```text
0.50 = 50%

0.80 = 80%

0.93 = 93%

1.00 = 100%
```

Suppose an airline checks 200 passengers every day and records the proportion whose luggage reaches the correct destination.

Example:

```text
Day 1 = 0.89

Day 2 = 0.91

Day 3 = 0.93
```

The p chart helps determine whether this proportion is statistically stable over time.

---

## Average Proportion

The application first calculates:

```text
p̄ = Average Proportion
```

It then calculates the standard error:

```text
σp = √[p̄(1-p̄) / n]
```

where:

```text
p̄ = Average proportion

n = Sample size
```

The 3-sigma limits are:

```text
UCL = p̄ + 3σp

LCL = p̄ - 3σp
```

Because a proportion cannot be below 0 or above 1, the application constrains the limits to:

```text
0 ≤ p ≤ 1
```

---

## Important Note About p Charts

In Statistical Process Control, p charts are commonly presented using the **fraction nonconforming/defective**.

This educational application can also process a consistently defined proportion such as **proportion correct**, provided the meaning of the input is clearly stated.

---

# 4️⃣ Acceptance Sampling

## What Is Acceptance Sampling?

Acceptance Sampling helps decide whether to accept or reject a production lot by examining only a sample.

Suppose a company has:

```text
1,000 products
```

Inspecting every product may require unnecessary time and cost.

Instead, the company may inspect:

```text
100 products
```

A rule could be:

```text
0 or 1 defective
        ↓
ACCEPT LOT

2 or more defective
        ↓
REJECT LOT
```

This is called an **acceptance sampling plan**.

---

# 📦 Important Acceptance Sampling Terms

## Lot Size

Total number of items in the production lot.

Example:

```text
Lot Size = 1000
```

---

## Sample Size

Number of items inspected from the lot.

Example:

```text
Sample Size = 100
```

---

## Defect Probability

Estimated proportion of defective items.

Example:

```text
0.01 = 1%
```

For a lot of 1,000 items:

```text
1000 × 0.01 = 10
```

The model therefore represents approximately 10 defective items in the finite lot.

---

## Acceptance Number

The maximum number of defective items allowed in the sample while still accepting the lot.

Example:

```text
Acceptance Number = 1
```

means:

```text
0 defective → ACCEPT

1 defective → ACCEPT

2 defective → REJECT

3 defective → REJECT
```

and so on.

---

# 🧮 Three Acceptance Sampling Methods

The application compares three approaches.

## 1. Exact Hypergeometric Probability

The hypergeometric distribution is used when:

* the population/lot is finite,
* items are sampled without replacement,
* and the number of defective items in the lot is treated as fixed.

For example:

```text
Lot Size = 1000

Defective Items = 10

Sample Size = 100
```

When one item is selected, it is not placed back into the lot.

Therefore, sampling is **without replacement**.

The hypergeometric model accounts for this finite-population behavior.

---

## 2. Binomial Approximation

The application also calculates a binomial probability.

The binomial distribution treats the defect probability as effectively constant across draws.

It can provide a useful approximation in suitable sampling situations.

The application displays both results so they can be compared.

---

## 3. Monte Carlo Simulation

Monte Carlo simulation verifies the probability experimentally using repeated random sampling.

Suppose:

```text
Simulations = 10,000
```

The computer conceptually performs:

```text
Take random sample
        ↓
Count defective items
        ↓
Accept or reject
        ↓
Record result
        ↓
Repeat 10,000 times
```

Then:

```text
Simulated Acceptance Probability
=
Accepted Simulations / Total Simulations
```

If:

```text
7,300 out of 10,000
```

simulated lots are accepted, then:

```text
7300 / 10000

= 0.73

= 73%
```

---

# 🔬 Why Compare Theory and Simulation?

Suppose the exact mathematical result is:

```text
73%
```

and simulation produces:

```text
72.8%
```

The values are close.

That provides empirical evidence that the simulation agrees with the theoretical calculation.

The application reports:

```text
Exact Result
      ↓
Simulation Result
      ↓
Absolute Difference
      ↓
Verification
```

Monte Carlo results do not need to be perfectly identical to the theoretical value because simulation contains random sampling variation.

---

# 📏 Understanding Control Limits

Control limits are statistical boundaries calculated from process data.

The three important lines are:

```text
UCL
Upper Control Limit

---------------------

CL
Center Line

---------------------

LCL
Lower Control Limit
```

A control chart may look conceptually like:

```text
UCL  ----------------------------

              ●
       ●             ●
            ●
CL   ----------------------------
                 ●
         ●

LCL  ----------------------------
```

A point beyond a control limit can indicate special-cause variation that should be investigated.

---

# ⚠️ Control Limits Are NOT Specification Limits

This distinction is important.

**Control limits** describe statistical behavior based on process data.

**Specification limits** describe requirements or acceptable performance defined by a customer, organization, engineering design, or business rule.

Therefore:

```text
Process is statistically stable
```

does **not automatically mean**:

```text
Process meets the required target.
```

A process can be stable but consistently produce results that fail a business requirement.

---

# 📚 Textbook vs Custom Data

For the X-Bar, R, and p chart modules, the application provides three data modes.

## Mode 1 — Chapter 10 Textbook Example

```text
Chapter 10 Textbook Example
```

This mode loads the predefined example data used for the assignment.

Its purpose is to verify the manually solved numerical using software.

---

## Mode 2 — Enter Custom Data

```text
Enter Custom Data
```

This allows users to enter their own observations.

Example:

```text
10,12,11,13,12
9,11,10,12,11
13,14,12,13,15
10,11,12,10,9
11,12,13,11,12
```

For X-Bar and R charts:

```text
Each row = one sample

Each number in the row = one observation
```

All rows must contain the same number of observations.

---

## Mode 3 — Upload CSV

```text
Upload CSV
```

Users can upload datasets instead of manually entering every observation.

This makes the application reusable for other compatible datasets.

---

# 📁 CSV Upload

## X-Bar and R Chart Format

Example:

```csv
obs1,obs2,obs3,obs4,obs5
10,12,11,13,12
9,11,10,12,11
13,14,12,13,15
10,11,12,10,9
11,12,13,11,12
```

Interpretation:

```text
Row 1 = Sample 1
Row 2 = Sample 2
Row 3 = Sample 3
...
```

and:

```text
Columns = observations inside each sample
```

---

## p Chart CSV

A p-chart CSV may contain a proportion column such as:

```csv
day,proportion
1,0.89
2,0.91
3,0.93
4,0.95
5,0.94
```

After uploading the CSV, select the column containing the proportions.

All proportions must satisfy:

```text
0 ≤ proportion ≤ 1
```

---

# 📂 Project Structure

The basic project structure is:

```text
quality-control-simulation/
│
├── app.py
│
├── calculations.py
│
├── requirements.txt
└── README.md
```

## `app.py`

Contains the Streamlit user interface.

It handles:

* navigation,
* textbook/custom/CSV inputs,
* displaying results,
* tables,
* graphs,
* interpretation messages.

---

## `calculations.py`

Contains the statistical calculation engine.

It performs calculations for:

```text
X-Bar Chart
R Chart
p Chart
Acceptance Sampling
```

Keeping calculations separate from the user interface makes the project easier to understand, test, and maintain.

---

## `requirements.txt`

Contains the Python libraries required to run the project.

Example:

```text
streamlit
numpy
pandas
matplotlib
scipy
```

---

# 🛠 Technologies Used

## Python

Main programming language.

## Streamlit

Creates the interactive web application.

## NumPy

Performs numerical calculations and array operations.

## Pandas

Handles tabular data and CSV files.

## Matplotlib

Creates control charts and simulation graphs.

## SciPy

Provides statistical probability distributions such as:

```text
Binomial Distribution
Hypergeometric Distribution
```

---

# 💻 Installation

## Requirement

Install Python on your computer.

Python 3.10+ is recommended.

Check your Python installation:

```bash
python --version
```

---

## 1. Clone the Repository

```bash
git clone <YOUR-REPOSITORY-URL>
```

Move into the project:

```bash
cd quality-control-simulation
```

---

## 2. Create a Virtual Environment

### Windows

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

### macOS/Linux

```bash
python3 -m venv venv
```

Activate it:

```bash
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🚀 Running the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

Streamlit will normally open the application automatically in your browser.

A local address commonly looks like:

```text
http://localhost:8501
```

---

# 🧪 Example Inputs

## X-Bar / R Chart

Select:

```text
Enter Custom Data
```

and enter:

```text
10,12,11,13,12
9,11,10,12,11
13,14,12,13,15
10,11,12,10,9
11,12,13,11,12
```

Then click:

```text
Run X-Bar Analysis
```

or:

```text
Run R Chart Analysis
```

depending on the selected module.

---

## p Chart

Example:

```text
Sample Size = 200
```

Proportions:

```text
0.89,0.91,0.93,0.95,0.94,0.96,0.92
```

Then run the analysis.

---

## Acceptance Sampling

Example configuration:

```text
Lot Size = 1000

Sample Size = 100

Defect Probability = 0.01

Acceptance Number = 1

Monte Carlo Simulations = 10000
```

The application calculates:

```text
Exact Hypergeometric Probability

Binomial Approximation

Monte Carlo Probability

Difference
```

---

# 📊 Understanding the Results

## IN CONTROL

If the application displays:

```text
Process Status: IN CONTROL
```

it means no plotted point violated the application's calculated point-level control limits.

It does not guarantee perfect quality.

---

## OUT OF CONTROL

If the application displays:

```text
Process Status: OUT OF CONTROL
```

one or more observations crossed a calculated control limit.

The application also identifies the corresponding sample numbers.

This suggests that the process should be investigated for possible special causes.

---

# 🎲 Acceptance Sampling Simulation

The acceptance-sampling workflow is:

```text
User Inputs Sampling Plan
          ↓
Determine Finite Lot Composition
          ↓
Calculate Exact Hypergeometric Probability
          ↓
Calculate Binomial Approximation
          ↓
Run Monte Carlo Simulation
          ↓
Compare Results
          ↓
Calculate Difference
          ↓
Verification
```

The histogram displays how often different numbers of defective items appeared in the simulated samples.

---

# 🔁 Reproducibility

Monte Carlo simulations normally contain randomness.

The calculation engine uses a fixed random seed by default:

```text
seed = 42
```

This makes the simulation reproducible.

In other words, running the same simulation with the same inputs and seed should produce the same simulated sequence/results.

This is useful for:

* assignments,
* testing,
* demonstrations,
* result verification.

---

# ⚠️ Limitations

This project is primarily an **educational Quality Control simulation and verification system**.

Current limitations include:

### X-Bar and R Charts

The current implementation supports subgroup sizes:

```text
2 to 10
```

because the calculation engine currently contains the required statistical constants for these subgroup sizes.

---

### Equal Sample Sizes

The current p-chart implementation assumes the same sample size for every sample.

More advanced implementations can calculate varying control limits when sample sizes differ.

---

### Basic Control-Chart Detection

The current implementation primarily checks whether individual observations fall outside the calculated control limits.

A complete industrial Statistical Process Control system may additionally use rules for:

* long runs,
* trends,
* cycles,
* zones,
* consecutive points,
* other non-random patterns.

---

### Educational Use

This application should not be treated as a replacement for a validated industrial Quality Management System or professional statistical package.

Its primary purpose is:

```text
Learning
+
Calculation
+
Simulation
+
Visualization
+
Verification
```

---

# 🎯 Educational Purpose

This project demonstrates how theoretical statistical concepts can be converted into software.

It connects:

```text
Statistics
        +
Quality Control
        +
Python Programming
        +
Simulation
        +
Data Visualization
        +
Software Quality Engineering
```

Instead of only solving formulas manually, students can observe how changing input data changes:

* averages,
* ranges,
* proportions,
* control limits,
* process status,
* probabilities,
* simulation outcomes.

---

# 🔮 Future Improvements

Possible future improvements include:

* Support for larger subgroup sizes
* Variable-sample-size p charts
* c charts
* np charts
* u charts
* Process Capability Analysis
* Cp and Cpk
* Additional SPC run rules
* Downloadable analysis reports
* Export results to CSV
* Export charts as images
* Editable datasets directly in the browser
* More textbook numerical examples
* Automated comparison with manual answers
* Additional Acceptance Sampling plans
* Operating Characteristic (OC) curves
* Producer's Risk
* Consumer's Risk
* AQL/LTPD analysis

---

# 📌 Summary

The Quality Control Simulation System provides an interactive way to understand and verify important Statistical Quality Control techniques.

The project supports:

```text
X-Bar Control Chart
        ↓
Process Average

R Control Chart
        ↓
Process Variability

p Control Chart
        ↓
Process Proportion

Acceptance Sampling
        ↓
Lot Acceptance Probability
```

Users can work with:

```text
Textbook Data
     OR
Custom Data
     OR
CSV Data
```

The application then:

```text
Calculates
    ↓
Visualizes
    ↓
Simulates
    ↓
Compares
    ↓
Verifies
```

This makes the project useful both as an academic simulation assignment and as a beginner-friendly demonstration of how statistical Quality Control can be implemented using Python.

---

# 👨‍💻 Author

**Abdul Moiz**

Software Engineering Student

Project Area:

**Software Quality Engineering & Testing**

Project:

**Quality Control Numerical Verification & Simulation**

---

# 📚 Reference

**Statistics for Management, 8th Edition**

Chapter 10:

**Quality and Quality Control**

The project uses statistical concepts from the chapter for educational implementation and numerical verification.

---

# 📄 License

This project is intended for educational and academic use.

If you reuse or extend the project, please provide appropriate attribution where required.
