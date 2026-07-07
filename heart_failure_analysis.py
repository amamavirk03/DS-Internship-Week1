# DS Internship - Week 1 Assignment
# This script loads a medical dataset and looks at it step by step.

import pandas as pd

# STEP 1: Load the data
# This reads the CSV file and stores it in a table called patient_data
patient_data = pd.read_csv("heart.csv")

# STEP 2: Look at the basic structure of the data
print("Number of rows and columns:")
print(patient_data.shape)   # (rows, columns)

print("\nColumn names:")
print(patient_data.columns.tolist())

print("\nData types of each column:")
print(patient_data.dtypes)

# STEP 3: Get basic statistics (mean, median, standard deviation)
print("\nAverage (mean) of Age, RestingBP, Cholesterol:")
print(patient_data[["Age", "RestingBP", "Cholesterol"]].mean())

print("\nMedian of Age, RestingBP, Cholesterol:")
print(patient_data[["Age", "RestingBP", "Cholesterol"]].median())

print("\nStandard deviation of Age, RestingBP, Cholesterol:")
print(patient_data[["Age", "RestingBP", "Cholesterol"]].std())

# STEP 4: Filter the data
# We only want patients older than 50 AND with cholesterol above 200
older_high_cholesterol = patient_data[
    (patient_data["Age"] > 50) & (patient_data["Cholesterol"] > 200)
]

print("\nPatients older than 50 with cholesterol above 200:")
print(older_high_cholesterol.head(10))  # show only the first 10 rows