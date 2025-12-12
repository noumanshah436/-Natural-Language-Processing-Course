import pandas as pd

CSV_FILE = "IMDB_Dataset.csv"

# Load the dataset
df = pd.read_csv(CSV_FILE)

# Check the first few rows
print("First 5 rows:")
print(df.head())

# Find all unique classes in the 'sentiment' column
classes = df['sentiment'].unique()

print("\nUnique classes in the dataset:")
for cls in classes:
    print(f"- {cls}")
