## 🔄 Final Project Workflow

The purpose of **Part 2B** is to verify the Quality Control numericals solved manually in **Part 2A** by reproducing the calculations using Python and Streamlit.

### Overall Workflow

```text
Chapter 10 Numerical
        ↓
Solve Manually in Part 2A
        ↓
Select Same Numerical in Part 2B Application
        ↓
Application Loads Textbook Data
        ↓
Python Performs Statistical Calculation
        ↓
Calculate CL / UCL / LCL
or Acceptance-Sampling Risk
        ↓
Generate Control Chart where applicable
        ↓
Compare Expected Answer with Python Result
        ↓
Calculate Difference
        ↓
Verify Result
        ↓
Interpret Quality-Control Result
```

---

## 📊 Detailed Part 2B Workflow

```text
START
  │
  ▼
Open Streamlit Application
  │
  ▼
Select Analysis
  │
  ├── X-Bar Control Chart
  ├── R Control Chart
  ├── p Control Chart
  └── Acceptance Sampling
  │
  ▼
Select Textbook Numerical
  │
  ▼
Load Exact Chapter 10 Data
  │
  ▼
Display Given Values / Dataset
  │
  ▼
Perform Python Calculation
  │
  ├── X-Bar / R / p Chart
  │       │
  │       ├── Calculate Center Line (CL)
  │       ├── Calculate Upper Control Limit (UCL)
  │       └── Calculate Lower Control Limit (LCL)
  │
  └── Acceptance Sampling
          │
          ├── Calculate Acceptance Probability
          ├── Calculate Producer's Risk
          └── Calculate Consumer's Risk
  │
  ▼
Generate Results
  │
  ▼
Verify Results
  │
  ├── Self-Check Exercise
  │       ↓
  │   Book Worked Answer
  │
  └── Application / Review Exercise
          ↓
      Expected / Manual Result
  │
  ▼
Compare with Python Result
  │
  ▼
Calculate Difference
  │
  ▼
Is Difference Within Tolerance?
  │
  ├── YES
  │     ↓
  │   ✅ VERIFIED /
  │   COMPUTATION VERIFIED
  │
  └── NO
        ↓
      ⚠ Check Calculation,
      Constants or Rounding
  │
  ▼
Generate Control Chart
(where applicable)
  │
  ▼
Interpret Process
  │
  ├── In Control
  └── Out of Control
  │
  ▼
END
```

---

## 🧮 Verification Logic

The application uses two types of verification:

### 1. Self-Check Exercises

For Self-Check exercises where the textbook provides an official worked answer:

```text
Book Worked Answer
        ↓
Python Result
        ↓
Calculate Difference
        ↓
✅ VERIFIED AGAINST BOOK
```

### 2. Application / Review Exercises

For exercises where the textbook does not provide an explicit worked answer:

```text
Textbook Given Data
        ↓
Expected / Manual Result
        ↓
Python Result
        ↓
Calculate Difference
        ↓
✅ COMPUTATION VERIFIED
```

This avoids incorrectly labeling a software-calculated value as an official textbook answer.

---

## 📈 Analysis Methods

The application supports four main Quality Control methods:

```text
Quality Control Analysis
│
├── X-Bar Control Chart
│   └── Monitors changes in process mean
│
├── R Control Chart
│   └── Monitors process variability
│
├── p Control Chart
│   └── Monitors proportion of defective/
│       nonconforming observations
│
└── Acceptance Sampling
    ├── Acceptance Probability
    ├── Producer's Risk
    ├── Consumer's Risk
    └── OC-Curve Calculations
```

---

## 📉 OC-Curve Exercises

For OC-curve exercises, the textbook may require the probability to be estimated visually from a graph.

The application calculates the corresponding probability numerically using the binomial distribution.

Therefore:

```text
Textbook OC Curve
        ↓
Approximate Graph-Read Value

Python Application
        ↓
Numerically Calculated Value

Small Difference
        ↓
May Occur Due to Graph Reading / Rounding
```

---

## 📁 Project Structure

```text
Software-Testing-Simulation/
│
├── app.py
│   └── Streamlit interface, numerical selection,
│       result display and visualization
│
├── calculations.py
│   └── Statistical formulas and calculations
│
├── textbook_data.py
│   └── Chapter 10 textbook numerical datasets
│
├── requirements.txt
│   └── Required Python libraries
│
└── README.md
    └── Project documentation
```

---

## 🎯 Final Objective

The complete relationship between Part 2A and Part 2B is:

**Part 2A = Manual Calculation**

**Part 2B = Software Calculation + Visualization + Comparison + Verification**

The application demonstrates that Quality Control numericals solved manually can be reproduced and verified using software.
