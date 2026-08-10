import pandas as pd
import numpy as np

import scipy.stats as stats

import statsmodels.api as sm
import statsmodels.formula.api as smf

import plotly.express as px
import plotly.graph_objects as go

from statsmodels.stats.outliers_influence import variance_inflation_factor

df = pd.read_csv(
r"C:\Users\jolee\Desktop\StudentPerformanceFactors.csv"
)

print(df.shape)
print(df.info())
print(df.head())

# Data Quality Assessment

quality = pd.DataFrame({
    "Missing Values": df.isnull().sum(),
    "Missing %": round(
        (df.isnull().sum()/len(df))*100,
        2
    ),
    "Data Type": df.dtypes
})

print(quality)

# Descriptive Statistics

summary = df.describe().T

summary["Range"] = (
    summary["max"] -
    summary["min"]
)

print(summary)

# Student Performance Distribution

fig = px.histogram(
    df,
    x="Exam_Score",
    nbins=30,
    title="Distribution of Exam Scores"
)

fig.show()

# Top Academic Success Factors

numeric_cols = [
    "Hours_Studied",
    "Attendance",
    "Sleep_Hours",
    "Previous_Scores",
    "Tutoring_Sessions",
    "Physical_Activity",
    "Exam_Score"
]

corr = df[numeric_cols].corr()

fig = px.imshow(
    corr,
    text_auto=True,
    title="Academic Success Correlation Matrix"
)

fig.show()

# Study Hours Impact

study_hours = (
    df.groupby(
        pd.cut(
            df["Hours_Studied"],
            bins=5
        )
    )
    ["Exam_Score"]
    .mean()
)

print(study_hours)

# Gender Performance Analysis

gender_scores = (
    df.groupby("Gender")
    ["Exam_Score"]
    .agg([
        "count",
        "mean",
        "median",
        "std"
    ])
)

print(gender_scores)

# Statistical Test: Gender Difference

male_scores = df[
    df["Gender"]=="Male"
]["Exam_Score"]

female_scores = df[
    df["Gender"]=="Female"
]["Exam_Score"]

t_stat,p_value = stats.ttest_ind(
    male_scores,
    female_scores
)

print("T Statistic:",t_stat)
print("P Value:",p_value)

# Tutoring Effectiveness

tutoring = (
    df.groupby("Tutoring_Sessions")
    ["Exam_Score"]
    .mean()
    .reset_index()
)

fig = px.line(
    tutoring,
    x="Tutoring_Sessions",
    y="Exam_Score",
    markers=True,
    title="Impact of Tutoring on Performance"
)

fig.show()

# Sleep Quality Analysis

sleep_analysis = (
    df.groupby(
        pd.cut(
            df["Sleep_Hours"],
            bins=[0,5,6,7,8,10]
        )
    )
    ["Exam_Score"]
    .mean()
)

print(sleep_analysis)

# High-Performing Student Profile

top_students = df[
    df["Exam_Score"]
    >= df["Exam_Score"].quantile(.75)
]

profile = top_students[
[
"Hours_Studied",
"Attendance",
"Sleep_Hours",
"Tutoring_Sessions",
"Previous_Scores"
]
].mean()

print(profile)

# Profile Visualization

profile_df = profile.reset_index()

profile_df.columns = [
    "Metric",
    "Average"
]

fig = px.bar(
    profile_df,
    x="Metric",
    y="Average",
    title="Characteristics of High-Performing Students"
)

fig.show() 

# Educational Success Model

model = smf.ols(
"""
Exam_Score
~
Hours_Studied
+
Attendance
+
Sleep_Hours
+
Previous_Scores
+
Tutoring_Sessions
+
Physical_Activity
""",
data=df
).fit()

print(model.summary())

# Sample Data with model Visualization

coefficients = pd.DataFrame({
    "Variable": model.params.index,
    "Coefficient": model.params.values
})

fig = px.bar(
    coefficients,
    x="Variable",
    y="Coefficient",
    title="Factors Influencing Exam Scores"
)

fig.show()

#  Student Segmentation

df["Performance_Group"] = pd.qcut(
    df["Exam_Score"],
    q=4,
    labels=[
        "Low",
        "Medium",
        "High",
        "Excellent"
    ]
)

segment_summary = (
    df.groupby("Performance_Group")
    .agg({
        "Hours_Studied":"mean",
        "Attendance":"mean",
        "Sleep_Hours":"mean",
        "Tutoring_Sessions":"mean",
        "Exam_Score":"mean"
    })
)

print(segment_summary)