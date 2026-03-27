import pandas as pd

# Step 1: Create a sample dataset
data = {
    "Name": ["Alice", "Bob", "Alice", "Charlie", None],
    "Age": [25, 30, 25, None, 22],
    "Gender": ["Female", "male", "FEMALE", "Male ", "female"]
}

df = pd.DataFrame(data)

print("Original Dataset:\n")
print(df)

# Step 2: Handle Missing Values
df["Age"].fillna(df["Age"].mean(), inplace=True)
df["Name"].fillna("Unknown", inplace=True)

# Step 3: Remove Duplicates
df = df.drop_duplicates()

# Step 4: Standardize Text
df["Gender"] = df["Gender"].str.lower().str.strip()

print("\nCleaned Dataset:\n")
print(df)