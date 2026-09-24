# 📊 Quality Control Simulation System

[![Live Demo](https://img.shields.io/badge/Live%20Demo-Streamlit-FF4B4B?logo=streamlit\&logoColor=white)](https://software-testing-simulation-abdulmoiz-b22110106002.streamlit.app/)
[![GitHub](https://img.shields.io/badge/Source%20Code-GitHub-181717?logo=github\&logoColor=white)](https://github.com/Abdul-moiz123/Software-Testing-Simulation)
![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python\&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B?logo=streamlit\&logoColor=white)

A beginner-friendly web application for **simulating, calculating, visualizing, and verifying Statistical Quality Control techniques**.

This project was developed for **Software Quality Engineering & Testing — Part 2B**, where simulation tools are used to verify manually solved Quality Control numericals.

---

## 🚀 Live Application

### 👉 [Open the Quality Control Simulation System](https://software-testing-simulation-abdulmoiz-b22110106002.streamlit.app/)

You can use the application directly in your browser. No installation is required.

### 💻 Source Code

👉 [GitHub Repository](https://github.com/Abdul-moiz123/Software-Testing-Simulation)

---

# 📖 Table of Contents

1. [What Is This Project?](#-what-is-this-project)
2. [Why Was It Created?](#-why-was-it-created)
3. [What Is Quality Control?](#-what-is-quality-control)
4. [What Does Verification Mean?](#-what-does-verification-mean)
5. [Main Features](#-main-features)
6. [How the System Works](#-how-the-system-works)
7. [X-Bar Control Chart](#1-x-bar-control-chart)
8. [R Control Chart](#2-r-control-chart)
9. [p Control Chart](#3-p-control-chart)
10. [Acceptance Sampling](#4-acceptance-sampling)
11. [Data Input Methods](#-data-input-methods)
12. [CSV Format](#-csv-format)
13. [Project Structure](#-project-structure)
14. [Technologies Used](#-technologies-used)
15. [Installation](#-installation)
16. [Running the Application](#-running-the-application)
17. [How to Use the Application](#-how-to-use-the-application)
18. [Example Inputs](#-example-inputs)
19. [Understanding Results](#-understanding-the-results)
20. [Important Statistical Notes](#-important-statistical-notes)
21. [Limitations](#-limitations)
22. [Deployment](#-deployment)
23. [Future Improvements](#-future-improvements)
24. [Author](#-author)
25. [Reference](#-reference)

---

# 🎯 What Is This Project?

The **Quality Control Simulation System** is an interactive web application that helps users understand and verify Statistical Quality Control calculations.

Normally, students solve Quality Control numerical problems manually using mathematical formulas.

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
Interpret the Process
```

This application performs these calculations automatically.

It also generates graphs so users can visually understand the results.

The complete workflow is:

```text
Manual / Textbook Numerical
          ↓
Enter the Same Data
          ↓
Python Performs Calculations
          ↓
Statistical Results Generated
          ↓
Graph Generated
          ↓
Compare Manual and Software Results
          ↓
Verification
```

If the software calculation agrees with the manually calculated result, the numerical has been computationally verified.

---

# 🎓 Why Was It Created?

This project was developed for the university course:

**Software Quality Engineering & Testing**

Specifically:

**Part 2B — Use simulation tools to verify the results of Quality Control numericals.**

The statistical topics implemented in the application are based on concepts from:

**Statistics for Management, 8th Edition**

Chapter 10:

**Quality and Quality Control**

Instead of only solving calculations manually, this project demonstrates how the same Quality Control techniques can be implemented and verified using software.

---

# 🏭 What Is Quality Control?

Quality Control is the process of checking whether a product, service, or process is operating consistently and at an acceptable level.

For example, imagine a factory filling bottles.

The target amount is:

```text
500 ml
```

Actual bottles might contain:

```text
498 ml
501 ml
500 ml
503 ml
497 ml
```

Some variation is normal.

The important question is:

> Is this normal process variation, or has something unusual happened?

Statistical Quality Control helps answer this question using data and statistical methods.

---

# 🔍 What Does Verification Mean?

Suppose a Quality Control numerical is solved manually.

The manual calculation gives:

```text
Grand Mean = 63.00
```

The same dataset is entered into this application.

Python also calculates:

```text
Grand Mean = 63.00
```

The software result agrees with the manual result.

Therefore, the calculation has been **computationally verified**.

For simulation-based methods such as Acceptance Sampling, verification also involves comparing:

```text
Exact Mathematical Probability
          ↓
Binomial Approximation
          ↓
Monte Carlo Simulation
```

If the simulation produces a result close to the theoretical probability, it provides additional computational verification.

---

# ✨ Main Features

The application currently supports:

* 📊 **X-Bar Control Chart**
* 📈 **R Control Chart**
* 📉 **p Control Chart**
* 🎲 **Acceptance Sampling**
* 🧮 Automatic statistical calculations
* 📋 Calculation and result tables
* 📈 Automatic control-chart generation
* 🚨 Detection of points outside control limits
* 📚 Built-in textbook examples
* ✍️ Custom data entry
* 📁 CSV file upload
* 🎲 Monte Carlo simulation
* 🔢 Exact Hypergeometric probability
* 🔬 Binomial approximation
* 🔄 Theoretical vs simulated result comparison
* 🌐 Interactive Streamlit web interface
* ☁️ Public cloud deployment

---

# ⚙️ How the System Works

The application contains four major Quality Control modules:

```text
Quality Control Simulation System
│
├── 1. X-Bar Control Chart
│
├── 2. R Control Chart
│
├── 3. p Control Chart
│
└── 4. Acceptance Sampling
```

Each module answers a different Quality Control question.

| Method              | What It Checks                                                               |
| ------------------- | ---------------------------------------------------------------------------- |
| X-Bar Chart         | Is the process average statistically stable?                                 |
| R Chart             | Is the process variability statistically stable?                             |
| p Chart             | Is the observed proportion statistically stable?                             |
| Acceptance Sampling | What is the probability that a lot will be accepted under the sampling plan? |

---

# 1. X-Bar Control Chart

## What Is an X-Bar Chart?

An **X-Bar Control Chart** monitors the average or mean of a process over time.

Instead of analyzing every observation separately, observations are divided into groups called **samples** or **subgroups**.

Example:

```text
Sample 1:
63, 55, 56, 53, 61, 64

Sample 2:
60, 63, 60, 65, 61, 66
```

The mean of each sample is calculated.

For example:

```text
10, 12, 11, 13, 12
```

The mean is:

```text
(10 + 12 + 11 + 13 + 12) / 5

= 11.6
```

The same calculation is performed for every sample.

---

## Grand Mean

After calculating all sample means, the application calculates the **Grand Mean**.

```text
Grand Mean
=
Average of all sample means
```

The Grand Mean becomes the **Center Line** of the X-Bar Control Chart.

---

## X-Bar Control Limits

The application calculates three important values:

```text
UCL = Upper Control Limit

CL = Center Line

LCL = Lower Control Limit
```

The implementation uses:

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

## How to Interpret an X-Bar Chart

A simplified interpretation is:

```text
Point inside limits
        ↓
No point-level control-limit violation
```

While:

```text
Point outside limits
        ↓
Possible special-cause variation
```

The application automatically detects sample means that fall outside the calculated limits.

---

# 2. R Control Chart

## What Is an R Chart?

The **R Control Chart** monitors the amount of variation or spread inside samples.

While the X-Bar chart checks the **average**, the R chart checks the **variability**.

For every sample:

```text
Range = Maximum Value - Minimum Value
```

Example:

```text
Sample:

10, 12, 15, 11, 13
```

Maximum:

```text
15
```

Minimum:

```text
10
```

Therefore:

```text
Range = 15 - 10

Range = 5
```

The same calculation is performed for every sample.

---

## Average Range

After calculating all sample ranges:

```text
R̄ = Average of all sample ranges
```

The Average Range becomes the center line of the R chart.

---

## Why Is an R Chart Important?

Consider two processes.

### Process A

```text
49, 50, 51, 50, 50
```

### Process B

```text
30, 70, 40, 60, 50
```

Both can have a similar average.

However, Process B has much greater variation.

Therefore, checking only the average is not enough.

The R chart helps determine whether the amount of process variation remains statistically stable.

---

# 3. p Control Chart

## What Is a p Chart?

A **p Control Chart** monitors a proportion.

A proportion is a value between:

```text
0 and 1
```

Examples:

```text
0.50 = 50%

0.80 = 80%

0.93 = 93%

1.00 = 100%
```

For example, an airline may inspect 200 passengers each day and record the proportion whose luggage reaches the correct destination.

```text
Day 1 = 0.89

Day 2 = 0.91

Day 3 = 0.93
```

The p chart helps determine whether this proportion remains statistically stable.

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

Where:

```text
p̄ = Average proportion

n = Sample size
```

The control limits are:

```text
UCL = p̄ + 3σp

LCL = p̄ - 3σp
```

Because proportions cannot be below 0 or above 1, the application constrains the limits to:

```text
0 ≤ p ≤ 1
```

---

## Important p-Chart Note

In Statistical Process Control, p charts are commonly used to monitor the **fraction nonconforming or defective**.

This educational application can also process another consistently defined proportion, such as **proportion correct**, as long as the user understands what the proportion represents.

---

# 4. Acceptance Sampling

## What Is Acceptance Sampling?

Acceptance Sampling helps determine whether a production lot should be accepted or rejected by inspecting only a sample from the lot.

Suppose a company produces:

```text
1,000 products
```

Inspecting every single product may take too much time.

Instead, the company might inspect:

```text
100 products
```

The sampling rule could be:

```text
0 or 1 defective
        ↓
ACCEPT LOT
```

and:

```text
2 or more defective
        ↓
REJECT LOT
```

This is called an **Acceptance Sampling Plan**.

---

# 📦 Important Acceptance Sampling Terms

## Lot Size

The total number of items in the production lot.

Example:

```text
Lot Size = 1000
```

---

## Sample Size

The number of items selected from the lot for inspection.

Example:

```text
Sample Size = 100
```

---

## Defect Probability

The estimated proportion of defective items.

Example:

```text
0.01 = 1%
```

If the lot contains 1,000 products:

```text
1000 × 0.01 = 10
```

This corresponds to approximately:

```text
10 defective items
```

in the finite-lot representation used by the application.

---

## Acceptance Number

The maximum number of defective items allowed in the inspected sample while still accepting the lot.

Example:

```text
Acceptance Number = 1
```

Therefore:

```text
0 defective → ACCEPT

1 defective → ACCEPT

2 defective → REJECT

3 defective → REJECT
```

and so on.

---

# 🧮 Acceptance Sampling Methods

The application compares three methods.

## 1. Exact Hypergeometric Probability

The **Hypergeometric Distribution** is useful when:

* the population is finite,
* sampling occurs without replacement,
* and the number of defective items in the finite lot is represented as fixed.

Example:

```text
Lot Size = 1000

Defective Items = 10

Sample Size = 100
```

When an item is selected, it is not returned to the lot.

Therefore:

```text
Sampling = Without Replacement
```

The Hypergeometric Distribution accounts for this finite-population behavior.

---

## 2. Binomial Approximation

The application also calculates the probability using a **Binomial Distribution**.

The Binomial model treats the defect probability as effectively constant across draws.

It is displayed as an approximation so users can compare it with the exact finite-lot calculation.

---

## 3. Monte Carlo Simulation

Monte Carlo simulation verifies the probability experimentally.

Suppose:

```text
Number of Simulations = 10,000
```

The computer repeatedly performs:

```text
Select Random Sample
        ↓
Count Defective Items
        ↓
Accept or Reject
        ↓
Record Result
        ↓
Repeat 10,000 Times
```

The simulated acceptance probability is:

```text
Accepted Simulations
--------------------
Total Simulations
```

For example, if:

```text
7,300
```

out of:

```text
10,000
```

simulations result in acceptance:

```text
7300 / 10000

= 0.73

= 73%
```

---

# 🔬 Why Compare Theory and Simulation?

Suppose the exact mathematical probability is:

```text
73.00%
```

and Monte Carlo simulation produces:

```text
72.80%
```

These results are very close.

Therefore, the simulation provides evidence supporting the theoretical calculation.

The verification process is:

```text
Exact Probability
       ↓
Monte Carlo Probability
       ↓
Calculate Difference
       ↓
Compare
       ↓
Verification
```

Monte Carlo results do not need to be perfectly identical because simulation contains random sampling variation.

---

# 🗂 Data Input Methods

The application is **not limited to fixed data**.

For X-Bar, R, and p charts, users can work with multiple input methods.

---

## 1. Chapter 10 Textbook Example

Select:

```text
Chapter 10 Textbook Example
```

The application automatically loads the predefined example data.

This is useful for assignment verification:

```text
Manual Textbook Numerical
          ↓
Software Calculation
          ↓
Compare Results
```

---

## 2. Enter Custom Data

Users can enter their own data.

Example for X-Bar or R chart:

```text
10,12,11,13,12
9,11,10,12,11
13,14,12,13,15
10,11,12,10,9
11,12,13,11,12
```

Interpretation:

```text
Each row = One Sample

Each number = One Observation
```

All samples must contain the same number of observations.

---

## 3. Upload CSV

Users can also upload their own CSV datasets.

This makes the application reusable for datasets other than the built-in textbook examples.

---

# 📁 CSV Format

## X-Bar / R Chart CSV

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

Columns contain observations within each sample.

---

## p Chart CSV

Example:

```csv
day,proportion
1,0.89
2,0.91
3,0.93
4,0.95
5,0.94
```

After uploading the CSV, the user selects the column containing the proportions.

Every proportion must satisfy:

```text
0 ≤ proportion ≤ 1
```

---

# 📂 Project Structure

The project has intentionally been kept simple.

```text
Software-Testing-Simulation/
│
├── app.py
│
├── calculations.py
│
├── requirements.txt
│
└── README.md
```

---

## `app.py`

This is the main Streamlit application.

It handles:

```text
User Interface
      +
Navigation
      +
Input
      +
Tables
      +
Charts
      +
Result Presentation
```

It allows users to select Quality Control methods and enter data.

---

## `calculations.py`

This file contains the statistical calculation logic.

It performs:

```text
X-Bar Calculations

R Chart Calculations

p Chart Calculations

Acceptance Sampling Calculations

Monte Carlo Simulation
```

Separating calculations from the frontend makes the project easier to understand, maintain, and test.

---

## `requirements.txt`

This file contains the Python packages required to run the project.

The main dependencies are:

```text
streamlit
numpy
pandas
matplotlib
scipy
```

---

# 🛠 Technologies Used

| Technology                    | Purpose                               |
| ----------------------------- | ------------------------------------- |
| **Python**                    | Main programming language             |
| **Streamlit**                 | Interactive web interface             |
| **NumPy**                     | Numerical calculations                |
| **Pandas**                    | Tables and CSV processing             |
| **Matplotlib**                | Control charts and histograms         |
| **SciPy**                     | Statistical probability distributions |
| **Git**                       | Version control                       |
| **GitHub**                    | Source-code hosting                   |
| **Streamlit Community Cloud** | Public deployment                     |

---

# 💻 Installation

You do **not** need to install the project if you only want to use it.

Simply open:

### 👉 [Live Application](https://software-testing-simulation-abdulmoiz-b22110106002.streamlit.app/)

However, developers or students who want to run the source code locally can follow the steps below.

---

## Prerequisite

Install **Python 3.10 or newer**.

Check your Python installation:

```bash
python --version
```

---

## Step 1 — Clone the Repository

Open Terminal, PowerShell, or the VS Code terminal.

Run:

```bash
git clone https://github.com/Abdul-moiz123/Software-Testing-Simulation.git
```

Enter the project directory:

```bash
cd Software-Testing-Simulation
```

---

## Step 2 — Create a Virtual Environment

### Windows

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

### macOS / Linux

```bash
python3 -m venv venv
```

Activate it:

```bash
source venv/bin/activate
```

---

## Step 3 — Install Dependencies

Run:

```bash
pip install -r requirements.txt
```

This installs all required Python libraries.

---

# 🚀 Running the Application

After installing the dependencies, run:

```bash
streamlit run app.py
```

Streamlit should automatically open the application in your web browser.

The default local address is normally:

```text
http://localhost:8501
```

---

# 🧭 How to Use the Application

The application is designed to be simple.

### Step 1

Open:

### 👉 [Quality Control Simulation System](https://software-testing-simulation-abdulmoiz-b22110106002.streamlit.app/)

### Step 2

Use the sidebar to select:

```text
X-Bar Control Chart

R Control Chart

p Control Chart

Acceptance Sampling
```

### Step 3

For X-Bar, R, or p chart, choose a data source:

```text
Chapter 10 Textbook Example

OR

Enter Custom Data

OR

Upload CSV
```

### Step 4

Review your input data.

### Step 5

Click:

```text
Run Analysis
```

### Step 6

The application calculates the required statistical values.

### Step 7

Review:

```text
Calculated Results

Control Limits

Process Status

Tables

Graphs

Interpretation
```

### Step 8

If this is a textbook numerical, compare the software result with your manually calculated result.

---

# 🧪 Example Inputs

## X-Bar / R Chart

Select:

```text
Enter Custom Data
```

Enter:

```text
10,12,11,13,12
9,11,10,12,11
13,14,12,13,15
10,11,12,10,9
11,12,13,11,12
```

Then run the analysis.

---

## p Chart

Example:

```text
Sample Size = 200
```

Enter:

```text
0.89,0.91,0.93,0.95,0.94,0.96,0.92
```

Then run the p-chart analysis.

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

The system calculates:

```text
Exact Hypergeometric Probability

Binomial Approximation

Monte Carlo Probability

Difference
```

It also generates a simulation histogram.

---

# 📊 Understanding the Results

## 🟢 IN CONTROL

If the application displays:

```text
Process Status: IN CONTROL
```

it means no plotted point crossed the application's calculated point-level control limits.

This does **not** mean the process is perfect.

It means the observed points did not violate those control limits.

---

## 🔴 OUT OF CONTROL

If the application displays:

```text
Process Status: OUT OF CONTROL
```

one or more plotted observations crossed a calculated control limit.

The application identifies the affected sample numbers.

This may indicate **special-cause variation** that should be investigated.

---

# ⚠️ Important Statistical Notes

## Control Limits Are NOT Specification Limits

This is a very important distinction.

### Control Limits

Control limits describe the statistical behavior of the process.

Examples:

```text
UCL

Center Line

LCL
```

### Specification Limits

Specification limits describe what is acceptable according to:

* customer requirements,
* engineering requirements,
* business requirements,
* product specifications.

Therefore:

```text
Process is statistically stable
```

does **not automatically mean**:

```text
Process meets the required target.
```

A process can be statistically stable but still consistently produce an unacceptable result.

---

# 🎲 Monte Carlo Results Are Approximate

Monte Carlo simulation uses repeated random experiments.

Therefore:

```text
Exact Result
```

and:

```text
Simulation Result
```

may be slightly different.

For example:

```text
Exact = 73.00%

Simulation = 72.82%
```

This small difference is expected.

Increasing the number of simulations generally reduces random simulation error.

---

# 🔁 Reproducibility

The simulation engine uses a fixed random seed by default:

```text
seed = 42
```

This makes the simulation reproducible.

In simple words:

> The same inputs should produce the same simulated sequence/results when the same seed is used.

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

because the calculation engine currently contains the required statistical constants for those subgroup sizes.

---

### p Chart

The current p-chart implementation assumes an equal sample size for all samples.

More advanced p charts can support different sample sizes and therefore changing control limits.

---

### Control-Chart Detection

The current application primarily checks whether individual plotted points fall outside the calculated control limits.

Advanced Statistical Process Control systems may additionally check:

* trends,
* long runs,
* zones,
* cycles,
* consecutive points,
* Nelson rules,
* Western Electric rules.

---

### Educational Use

This application is designed for:

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

It is **not intended to replace a validated industrial Quality Management System or professional statistical software package**.

---

# ☁️ Deployment

The project is publicly deployed using **Streamlit Community Cloud**.

## Live Deployment

### 🌐 [Open Live Application](https://software-testing-simulation-abdulmoiz-b22110106002.streamlit.app/)

The deployment architecture is:

```text
Python Source Code
        ↓
GitHub Repository
        ↓
Streamlit Community Cloud
        ↓
Public Web Application
```

This means users do not need Python installed to use the deployed application.

They only need a web browser and internet connection.

---

# 🔄 Overall Project Workflow

The complete project can be summarized as:

```text
              QUALITY CONTROL PROBLEM
                        │
                        ▼
                 Select Method
                        │
        ┌───────────────┼────────────────┐
        │               │                │
        ▼               ▼                ▼
     X-Bar              R               p Chart
        │               │                │
        └───────────────┼────────────────┘
                        │
                        ▼
                 Select Data
                        │
          ┌─────────────┼─────────────┐
          │             │             │
          ▼             ▼             ▼
      Textbook        Custom         CSV
        Data           Data          Upload
          │             │             │
          └─────────────┼─────────────┘
                        │
                        ▼
               Statistical Engine
                        │
                        ▼
                   Results
                        │
                        ▼
                Control Chart
                        │
                        ▼
                Interpretation
                        │
                        ▼
                  Verification
```

Acceptance Sampling follows:

```text
Sampling Plan
      ↓
Exact Hypergeometric Calculation
      ↓
Binomial Approximation
      ↓
Monte Carlo Simulation
      ↓
Compare Results
      ↓
Verification
```

---

# 🎯 Educational Purpose

This project connects several areas of Software Engineering and Statistics:

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

Instead of only memorizing formulas, users can experiment with data and observe how changes affect:

* Sample Means
* Grand Mean
* Sample Ranges
* Average Range
* Proportions
* Upper Control Limit
* Lower Control Limit
* Process Status
* Acceptance Probability
* Simulation Results

This makes abstract statistical concepts easier to understand visually.

---

# 🔮 Future Improvements

Possible future extensions include:

* Support for larger subgroup sizes
* Variable-sample-size p charts
* c Control Charts
* np Control Charts
* u Control Charts
* Process Capability Analysis
* Cp
* Cpk
* Nelson Rules
* Western Electric Rules
* Downloadable PDF reports
* CSV result export
* Chart image export
* More textbook numerical examples
* Automated manual-result comparison
* Operating Characteristic (OC) Curves
* Producer's Risk
* Consumer's Risk
* AQL analysis
* LTPD analysis
* More Acceptance Sampling plans
* Automated statistical explanations

---

# 👨‍💻 Author

## Abdul Moiz

**Software Engineering Student**

### Course

**Software Quality Engineering & Testing**

### Project

**Quality Control Numerical Verification & Simulation**

### Live Application

🌐 [software-testing-simulation-abdulmoiz-b22110106002.streamlit.app](https://software-testing-simulation-abdulmoiz-b22110106002.streamlit.app/)

### GitHub Repository

💻 [github.com/Abdul-moiz123/Software-Testing-Simulation](https://github.com/Abdul-moiz123/Software-Testing-Simulation)

---

# 📚 Reference

**Statistics for Management, 8th Edition**

**Chapter 10 — Quality and Quality Control**

The project applies Statistical Quality Control concepts for educational implementation, calculation, visualization, simulation, and numerical verification.

---

# 📄 Usage

This repository is primarily intended for **educational and academic purposes**.

Students and developers are welcome to study, test, and extend the project while providing appropriate attribution where required.

---

# ⭐ Project Summary

In one sentence:

> **This project converts manually solved Statistical Quality Control numericals into an interactive Python-based simulation system that calculates, visualizes, and verifies the results.**

### 🚀 [Try the Live Application](https://software-testing-simulation-abdulmoiz-b22110106002.streamlit.app/)

### 💻 [View the Source Code](https://github.com/Abdul-moiz123/Software-Testing-Simulation)
