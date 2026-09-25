# 📊 Chapter 10 Quality Control Numerical Verification

A Streamlit application for **Software Quality Engineering & Testing — Part 2B**. It verifies multiple Quality Control numericals from **Chapter 10 — Quality and Quality Control** of *Statistics for Management, 8th Edition*.

## Purpose

```text
Part 2A handwritten numerical
          ↓
Select the same textbook numerical
          ↓
Python calculation / simulation
          ↓
Control chart or risk result
          ↓
Compare with book/manual solution
          ↓
Verification
```

The Part 2B interface intentionally contains **textbook numericals only**. Custom Data and CSV Upload have been removed.

## Included Numericals

### X-Bar Control Chart
- SC 10-1 (a–d)
- SC 10-2 — Altoona Tire
- 10-12 (a–d)
- 10-13 — Wilson Piston
- 10-14 — Emergency Medical Services
- 10-15 — Track Bicycle Bearings
- 10-16 — Northern White Metals
- 10-44 — Global Bank
- 10-50 — Reliance Storage Media

### R Control Chart
- SC 10-3 (a–d)
- SC 10-4 — Altoona Tire
- 10-17 (a–e)
- 10-19 — Wilson Piston
- 10-20 — Emergency Medical Services
- 10-21 — Track Bicycle Bearings
- 10-22 — Northern White Metals
- 10-45 — Global Bank
- 10-51 — Reliance Storage Media

### p Control Chart
- SC 10-5 (a–d)
- SC 10-6 — Meals on Wheels
- 10-24 (a–e)
- 10-25 — USA Airlines
- 10-26 — BioAssist
- 10-28 — Spacious Skies
- 10-40 — R&H Bloch
- 10-52 — Photomatic

### Acceptance Sampling
- SC 10-8 — Producer's Risk
- SC 10-9 — Consumer's Risk
- 10-36 / 10-37
- 10-38 / 10-39
- 10-47 / 10-48
- 10-55 / 10-56

## Statistical Methods

**X-Bar:** `UCL/LCL = X-double-bar ± 3R-bar/(d2√n)` when R-bar is used.

**R chart:** `UCL = D4 R-bar`, `LCL = D3 R-bar`.

**p chart:** `UCL/LCL = p ± 3√(p(1-p)/n)`. A textbook target p is used when one is specified.

**Acceptance sampling:** binomial cumulative probabilities are used for producer's risk and consumer's risk. OC-curve exercises are numerically evaluated using the sampling plan behind the curve.

## Verification

Self-Check questions with explicit worked answers can show:

```text
Book Answer | Python Result | Difference | VERIFIED
```

Application/review exercises without a worked answer are labeled for comparison with the student's handwritten Part 2A solution.

## Project Structure

```text
Software-Testing-Simulation/
├── app.py
├── calculations.py
├── textbook_data.py
├── requirements.txt
└── README.md
```

## Requirements

```text
streamlit
numpy
pandas
matplotlib
scipy
```

Install and run:

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Reference

*Statistics for Management, 8th Edition* — Richard I. Levin, David S. Rubin, Masood H. Siddiqui, Sanjay Rastogi. Chapter 10: **Quality and Quality Control**.

## Author

**Abdul Moiz**  
Software Engineering Student  
Software Quality Engineering & Testing — Part 2B
