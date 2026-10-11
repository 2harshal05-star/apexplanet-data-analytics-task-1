
import pandas as pd

data = [
    ["Order_ID", "Order identifier", "Text", "Identifies order records"],
    ["Order_Date", "Date of order", "Date", "Analyzes sales over time"],
    ["Customer_ID", "Customer identifier", "Text", "Identifies customers"],
    ["Customer_Name", "Customer name", "Text", "Customer reference"],
    ["Age", "Customer age", "Number", "Customer demographic analysis"],
    ["Gender", "Customer gender", "Text", "Demographic analysis"],
    ["City", "Customer city", "Text", "Geographic sales analysis"],
    ["Product", "Purchased product", "Text", "Product performance"],
    ["Category", "Product category", "Text", "Category performance"],
    ["Quantity", "Number of items purchased", "Integer", "Sales volume"],
    ["Unit_Price", "Price per item", "Decimal", "Pricing analysis"],
    ["Total_Sales", "Total sales value", "Decimal", "Revenue analysis"]
]

columns = [
    "Column Name",
    "Meaning",
    "Data Type",
    "Business Relevance"
]

dictionary = pd.DataFrame(data, columns=columns)

dictionary.to_excel("data_dictionary.xlsx", index=False)

print("Data dictionary created successfully!")
