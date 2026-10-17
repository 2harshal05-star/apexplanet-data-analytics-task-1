
# ApexPlanet Data Analytics Internship
## Task 1 - Data Immersion & Wrangling

### Objective
To explore, clean, and prepare a sales dataset for further analysis.

### Dataset
The dataset provided by ApexPlanet contains 1,000 records and 12 columns covering customer, product, and sales information.

### Data Quality Issues Identified
- 20 missing Age values
- 13 missing City values
- 8 repeated Order_ID occurrences
- 0 exact duplicate rows
- 0 sales calculation mismatches

### Data Cleaning Performed
1. Checked for exact duplicate records.
2. Filled missing Age values using the median.
3. Replaced missing City values with "Unknown".
4. Converted Order_Date to datetime format.
5. Removed unnecessary spaces from selected text columns.
6. Verified Total_Sales against Quantity * Unit_Price.
7. Retained repeated Order_ID records for further investigation.

### Final Results
- Original records: 1,000
- Cleaned records: 1,000
- Missing values remaining: 0
- Exact duplicate rows remaining: 0
- Repeated Order_ID occurrences: 8 (unresolved)

### Tools Used
- Python
- Pandas
- OpenPyXL
- Visual Studio Code

### Project Files
- cleaning.py - Data cleaning script
- create_dictionary.py - Data dictionary generation
- data_dictionary.xlsx - Description of dataset columns
- output/cleaned_dataset.xlsx - Cleaned dataset

### Conclusion
The dataset has been cleaned and prepared for further analysis. The repeated Order_ID issue has been documented and requires clarification before treating Order_ID as a unique transaction identifier.


### Outlier Investigation
The IQR method was used to identify potential outliers in Age,
Quantity, Unit_Price, and Total_Sales.

- Age: 0 potential outliers
- Quantity: 0 potential outliers
- Unit_Price: 0 potential outliers
- Total_Sales: 19 potential outliers

The 19 high sales values were retained because outlier detection
alone does not establish that a record is erroneous. The sales
calculation check found no mismatches.

Detailed results are available in output/outlier_report.xlsx.


### Project Files

- `cleaning.py` - Data cleaning script
- `create_dictionary.py` - Data dictionary generation script
- `outlier_check.py` - Outlier detection script using the IQR method
- `data_dictionary.xlsx` - Description of dataset columns
- `data/ApexPlanet_DataAnalytics_Dataset.xlsx` - Original dataset
- `output/cleaned_dataset.xlsx` - Cleaned dataset
- `output/outlier_report.xlsx` - Outlier investigation report
