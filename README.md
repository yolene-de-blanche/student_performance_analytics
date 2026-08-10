
# 📚 Student Performance Analytics: Understanding the Drivers of Academic Success


# Project Overview

Educational institutions collect vast amounts of student data, but understanding which factors truly influence academic performance remains a challenge.

This project investigates the key drivers of student success using a dataset of **6,607 students** across academic, behavioral, and demographic dimensions.

The analysis seeks to answer one central question:

> What separates high-performing students from their peers?

---

# Business Problem

Schools and educational institutions continuously invest in tutoring programs, attendance initiatives, and academic support systems.

However, decision-makers often struggle to determine:

* Which factors have the strongest relationship with student performance?
* Do tutoring programs significantly improve outcomes?
* How important is attendance compared to study effort?
* What characteristics define high-performing students?

This project uses data analytics to provide evidence-based answers.

---

# Dataset Overview

### Dataset Size

* 6,607 Students
* 20 Variables

### Academic Variables

* Hours Studied
* Attendance
* Previous Scores
* Exam Score

### Student Wellbeing Variables

* Sleep Hours
* Physical Activity

### Support Variables

* Tutoring Sessions
* Access to Resources
* Internet Access

### Family Variables

* Family Income
* Parental Education
* Parental Involvement

### School Variables

* Teacher Quality
* School Type
* Peer Influence

---

# Project Objectives

### Objective 1

Analyze the distribution of student exam scores.

### Objective 2

Identify variables most strongly associated with academic performance.

### Objective 3

Measure the impact of tutoring on exam outcomes.

### Objective 4

Profile high-performing students.

### Objective 5

Generate actionable recommendations for educators.

---

# Exploratory Data Analysis

## Exam Score Distribution

The distribution of exam scores followed an approximately normal pattern centered around the mid-to-high 60s.

### Key Observation

Most students scored between:

```text
63 – 72
```

Very few students achieved extremely low or extremely high scores.

This indicates a relatively stable academic population with limited extreme outliers.

---

# Correlation Analysis

## Academic Success Correlation Matrix

### Correlation with Exam Scores

| Variable          | Correlation |
| ----------------- | ----------: |
| Attendance        |       0.581 |
| Hours Studied     |       0.445 |
| Previous Scores   |       0.175 |
| Tutoring Sessions |       0.157 |
| Physical Activity |       0.028 |
| Sleep Hours       |      -0.017 |

---

## Key Insights

### Attendance Was the Strongest Predictor

Attendance demonstrated the strongest positive relationship with exam performance.

### Study Time Matters

Students who invested more hours studying generally achieved higher exam scores.

### Sleep Had Minimal Direct Impact

Sleep hours showed virtually no direct relationship with exam scores within this dataset.

---

# Tutoring Impact Analysis

### Average Exam Score by Tutoring Sessions

The analysis revealed a positive relationship between tutoring frequency and academic performance.

### Observation

Student performance improved steadily as tutoring participation increased.

However, gains began to plateau after approximately six sessions.

### Interpretation

This suggests diminishing returns from excessive tutoring and highlights the importance of tutoring quality over quantity.

---

# Student Segmentation Analysis

Students were grouped into four performance categories:

* Low
* Medium
* High
* Excellent

---

## Characteristics of High-Performing Students

| Metric            | Excellent Students |
| ----------------- | -----------------: |
| Hours Studied     |               23.9 |
| Attendance        |               90.0 |
| Sleep Hours       |                7.0 |
| Tutoring Sessions |                1.8 |
| Previous Scores   |               78.0 |

---

## Performance Group Comparison

| Performance Group | Exam Score |
| ----------------- | ---------: |
| Low               |       63.3 |
| Medium            |       66.5 |
| High              |       68.5 |
| Excellent         |       72.0 |

---

# Visualisations
<img width="1824" height="813" alt="Screenshot_7-8-2026_12207_127 0 0 1" src="https://github.com/user-attachments/assets/65323b4c-394b-4454-b078-2e4e090a082b" />

<img width="1835" height="784" alt="Screenshot_7-8-2026_12212_127 0 0 1" src="https://github.com/user-attachments/assets/81e3c924-c923-414e-9176-3473c45768f8" />

<img width="1828" height="803" alt="Screenshot_7-8-2026_121934_127 0 0 1" src="https://github.com/user-attachments/assets/d3eb41e0-562b-4089-bbb5-91c15d247351" />

<img width="1806" height="775" alt="Screenshot_7-8-2026_122030_127 0 0 1" src="https://github.com/user-attachments/assets/aa309ae8-7c55-4073-9839-69eb8f9a86a2" />


# Key Findings

## Finding 1

Attendance is the strongest measurable driver of academic success.

## Finding 2

Students who study more consistently achieve better outcomes.

## Finding 3

Tutoring improves performance but exhibits diminishing returns.

## Finding 4

Previous academic performance remains an important indicator of future success.

## Finding 5

Academic achievement is influenced by multiple interconnected factors rather than a single variable.

---

# Recommendations

### For Schools

* Improve attendance monitoring systems.
* Develop early-warning systems for absenteeism.
* Expand targeted tutoring programs.

### For Educators

* Encourage structured study habits.
* Identify students with declining attendance patterns.

### For Policymakers

* Invest in attendance-focused interventions.
* Prioritize student engagement initiatives.

---

# Technologies Used

* Python
* Pandas
* NumPy
* Statsmodels
* SciPy
* Plotly
* Jupyter Notebook

---

# Skills Demonstrated

* Data Cleaning
* Exploratory Data Analysis
* Correlation Analysis
* Statistical Modeling
* Educational Analytics
* Student Segmentation
* Data Visualization
* Data Storytelling
* Business Intelligence

---

# Conclusion

This project demonstrates that academic success is driven more by consistent engagement than by any single intervention.

The strongest predictors of performance were attendance and study effort, while factors commonly assumed to influence outcomes—such as sleep and physical activity—showed limited direct relationships in this dataset.

The findings reinforce a simple but powerful insight:

> Students who consistently show up, stay engaged, and invest time in learning are most likely to succeed.
