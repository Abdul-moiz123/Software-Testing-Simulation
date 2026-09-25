SOFTWARE QUALITY ENGINEERING & TESTING
PART 2B — QUALITY CONTROL SIMULATION & VERIFICATION
Final Part 2B workflow should be presented like this:
                    START
                      │
                      ▼
        Open Streamlit Application
                      │
                      ▼
             Select Analysis
                      │
       ┌──────────────┼──────────────┬─────────────────┐
       ▼              ▼              ▼                 ▼
   X-Bar Chart     R Chart        p Chart       Acceptance Sampling
       │              │              │                 │
       └──────────────┴──────────────┴─────────────────┘
                      │
                      ▼
         Select Textbook Numerical
                      │
                      ▼
      Load Exact Chapter 10 Given Data
                      │
                      ▼
       Display Given Values / Dataset
                      │
                      ▼
            Calculate Using Python
                      │
          ┌───────────┴────────────┐
          ▼                        ▼
   Control Chart             Acceptance Sampling
 X-Bar / R / p Chart                │
          │                         ▼
          ▼                 Calculate Probability
 Calculate CL, UCL, LCL       / Producer's Risk /
          │                    Consumer's Risk
          └───────────┬────────────┘
                      │
                      ▼
              Generate Results
                      │
                      ▼
              Verify Results
                      │
             ┌────────┴────────┐
             ▼                 ▼
      Self-Check          Application /
       Exercise          Review Exercise
             │                 │
             ▼                 ▼
       Book Worked       Expected / Manual
          Answer              Result
             │                 │
             └────────┬────────┘
                      ▼
              Python Result
                      │
                      ▼
           Calculate Difference
                      │
                      ▼
        ┌─────────────┴─────────────┐
        ▼                           ▼
 Difference within             Difference not
    tolerance?                   acceptable?
        │                           │
       YES                          NO
        │                           │
        ▼                           ▼
  ✅ VERIFIED /              ⚠ Check Calculation,
COMPUTATION VERIFIED          Constants / Rounding
        │                           │
        └─────────────┬─────────────┘
                      ▼
           Display Visualization
              where applicable
                      │
                      ▼
          Interpret Process Status
        In Control / Out of Control
                      │
                      ▼
                     END


Part 2A → Part 2B complete workflow is:

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

Final Project Structure:

Software-Testing-Simulation/
│
├── app.py
│   └── Streamlit UI + selection + results + graphs
│
├── calculations.py
│   └── X-Bar, R, p-chart and acceptance-sampling formulas
│
├── textbook_data.py
│   └── Chapter 10 numerical datasets
│
├── requirements.txt
│   └── Python dependencies
│
└── README.md
    └── Project documentation