"""
DS Internship - Week 1 Assignment
Foundational Data Ingestion and Inspection Script
Dataset: Heart Failure Prediction (heart.csv)
Source: https://www.kaggle.com/datasets/fedesoriano/heart-failure-prediction

This script:
1. Loads the heart.csv dataset using Pandas
2. Inspects the dataset's shape, column names, and data types
3. Generates a statistical summary (mean, median, std) for numerical columns
4. Filters patients based on Age and Cholesterol conditions
"""

import pandas as pd

# ---------------------------------------------------------
# 1. DATA LOADING
# ---------------------------------------------------------
# Load the heart failure dataset into a Pandas DataFrame.
# Make sure 'heart.csv' is in the same folder as this script
# (downloaded manually from the Kaggle link above).
patient_data = pd.read_csv("heart.csv")

print("=" * 60)
print("HEART FAILURE PREDICTION DATASET - INSPECTION REPORT")
print("=" * 60)

# ---------------------------------------------------------
# 2. DATA INSPECTION
# ---------------------------------------------------------
# Print the shape (rows, columns) of the dataset.
print("\n--- Dataset Shape ---")
print(f"Rows: {patient_data.shape[0]}, Columns: {patient_data.shape[1]}")

# Print all column names in the dataset.
print("\n--- Column Names ---")
print(list(patient_data.columns))

# Print the data type of each column (int, float, object, etc.)
print("\n--- Data Types ---")
print(patient_data.dtypes)

# ---------------------------------------------------------
# 3. STATISTICAL SUMMARY
# ---------------------------------------------------------
# Generate mean, median, and standard deviation for all numerical columns.
print("\n--- Statistical Summary (All Numerical Columns) ---")
numerical_summary = patient_data.describe().T  # .T transposes for readability
numerical_summary["median"] = patient_data.median(numeric_only=True)
print(numerical_summary[["mean", "median", "std"]])

# Focused summary on three key clinical columns: Age, RestingBP, Cholesterol
print("\n--- Focused Summary: Age, RestingBP, Cholesterol ---")
key_columns = ["Age", "RestingBP", "Cholesterol"]
for column in key_columns:
    column_mean = patient_data[column].mean()
    column_median = patient_data[column].median()
    column_std = patient_data[column].std()
    print(f"\n{column}:")
    print(f"  Mean   = {column_mean:.2f}")
    print(f"  Median = {column_median:.2f}")
    print(f"  Std Dev= {column_std:.2f}")

# ---------------------------------------------------------
# 4. DATA FILTERING
# ---------------------------------------------------------
# Filter the dataset to only include patients where:
#   - Age is greater than 50
#   - Cholesterol is greater than 200
filtered_patients = patient_data[
    (patient_data["Age"] > 50) & (patient_data["Cholesterol"] > 200)
]

print("\n--- Filtered Data: Age > 50 and Cholesterol > 200 ---")
print(f"Number of matching patients: {filtered_patients.shape[0]}")
print("\nFirst 10 rows of filtered data:")
print(filtered_patients.head(10))

print("\n" + "=" * 60)
print("END OF REPORT")
print("=" * 60)
