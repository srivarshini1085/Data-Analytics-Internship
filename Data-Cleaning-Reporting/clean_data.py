import pandas as pd

# Load dataset
df = pd.read_csv("dataset.csv")

print("Original Data:")
print(df)

# Remove duplicates
df = df.drop_duplicates()

# Remove missing values
df = df.dropna()

# Save cleaned data
df.to_csv("cleaned_dataset.csv", index=False)

# Create report
report = f"""
DATA CLEANING REPORT
--------------------
Total Rows: {len(df)}
Total Columns: {len(df.columns)}

Columns:
{list(df.columns)}

Missing values removed
Duplicate rows removed

Data cleaning completed successfully.
"""

# Save report
with open("report.txt", "w") as file:
    file.write(report)

print("\nCleaned dataset saved!")
print("Report generated successfully!")