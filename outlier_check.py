
import pandas as pd

# Load the original dataset
df = pd.read_excel("data/ApexPlanet_DataAnalytics_Dataset.xlsx")

# Columns we want to investigate
columns = ["Age", "Quantity", "Unit_Price", "Total_Sales"]

for col in columns:
    values = df[col].dropna()

    # Calculate the IQR limits
    q1 = values.quantile(0.25)
    q3 = values.quantile(0.75)
    iqr = q3 - q1

    lower_limit = q1 - 1.5 * iqr
    upper_limit = q3 + 1.5 * iqr

    outliers = df[
        (df[col] < lower_limit) |
        (df[col] > upper_limit)
    ]

    print(f"\n--- {col} OUTLIER CHECK ---")
    print("Lower limit:", round(lower_limit, 2))
    print("Upper limit:", round(upper_limit, 2))
    print("Potential outliers:", len(outliers))

    if not outliers.empty:
        print(outliers[["Order_ID", col]].to_string(index=False))


# Save an outlier investigation report
report_rows = []

for col in columns:
    values = df[col].dropna()

    q1 = values.quantile(0.25)
    q3 = values.quantile(0.75)
    iqr = q3 - q1

    lower_limit = q1 - 1.5 * iqr
    upper_limit = q3 + 1.5 * iqr

    outliers = df[
        (df[col] < lower_limit) |
        (df[col] > upper_limit)
    ]

    report_rows.append({
        "Column": col,
        "Lower Limit": lower_limit,
        "Upper Limit": upper_limit,
        "Potential Outliers": len(outliers),
        "Action": (
            "Investigate; retain unless confirmed erroneous"
            if len(outliers) > 0
            else "No outliers flagged"
        )
    })

report = pd.DataFrame(report_rows)
report.to_excel("output/outlier_report.xlsx", index=False)

print("\nOutlier report saved to output/outlier_report.xlsx")
