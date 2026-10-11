
import pandas as pd
from pathlib import Path

# File locations
input_file = Path("data/ApexPlanet_DataAnalytics_Dataset.xlsx")
output_folder = Path("output")
output_folder.mkdir(exist_ok=True)

# Load the original dataset
df = pd.read_excel(input_file)

print("Original dataset shape:", df.shape)

# 1. Remove exact duplicate rows
df = df.drop_duplicates()

# 2. Handle missing Age values using the median
age_median = df["Age"].median()
df["Age"] = df["Age"].fillna(age_median)

# 3. Handle missing City values
df["City"] = df["City"].fillna("Unknown")

# 4. Convert Order_Date to a proper date
df["Order_Date"] = pd.to_datetime(
    df["Order_Date"], errors="coerce"
)

# 5. Standardize text columns
text_columns = [
    "Gender", "City", "Product", "Category"
]

for col in text_columns:
    df[col] = df[col].apply(
        lambda x: x.strip() if isinstance(x, str) else x
    )

# 6. Check repeated Order_ID values
repeated_ids = df["Order_ID"].duplicated().sum()
print("Repeated Order_ID rows retained for investigation:", repeated_ids)

# 7. Check sales calculation
expected_sales = df["Quantity"] * df["Unit_Price"]
mismatch = (
    df["Total_Sales"] - expected_sales
).abs() > 0.01

print("Sales calculation mismatches:", mismatch.sum())

# 8. Save cleaned dataset
output_file = output_folder / "cleaned_dataset.xlsx"
df.to_excel(output_file, index=False)

# 9. Final quality report
print("\n--- CLEANING SUMMARY ---")
print("Final dataset shape:", df.shape)
print("\nMissing values remaining:")
print(df.isnull().sum())
print("\nExact duplicate rows remaining:", df.duplicated().sum())
print("\nCleaned dataset saved to:", output_file)
