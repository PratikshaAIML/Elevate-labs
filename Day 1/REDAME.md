
Sales Dataset Cleaning 

Data Cleaning Task: Cleaned and preprocessed a sample Sales dataset using Python and Pandas. Handled missing values, removed duplicates, fixed inconsistent formatting, corrected totals, and exported a clean CSV file.

Task 1: Data Cleaning and Preprocessing

📁 Project Overview
This project involves cleaning and preprocessing a raw sales dataset using Python and Pandas. The dataset simulates real-world retail transactions including product details, customer info, and payment methods.

---

 📊 Dataset Details
- File Name: `sales_data.csv` (raw), `sales_data_cleaned.csv` (cleaned)
- Records: Sales transactions with fields like date, invoice ID, product, category, quantity, price, total, customer name, region, and payment method.

---

 🧹 Cleaning Steps Performed

The script performs the following data cleaning steps:

1. Loading the Dataset
   Loaded using `pandas.read_csv()`.

2. Handling Missing Values
   - Dropped rows containing any missing values using .dropna()`.

3. Removing Duplicates
   - Identified and removed duplicate rows using `.drop_duplicates()`.

4. Standardizing Text Columns
   - Trimmed whitespace and standardized case using `.str.strip().str.title()` for columns like `Payment Method`.
   - Fixed common typos (e.g., `'Csh'` → `'Cash'`).

5. Fixing Data Types
   - Converted `Date` column to datetime format.
   - Ensured `Quantity`, `Price`, and `Total` are numeric types.

6. Recalculating Totals
   - Verified and corrected the `Total` column with:  
     df['Total'] = df['Quantity'] * df['Price']
     

7. Exporting Cleaned Dataset
   - Saved the cleaned data as `sales_data_cleaned.csv`.

---

🧪 Tools & Libraries
- Python 3
- Pandas

---

 🚀 How to Run

1. Ensure `sales_data_dirty.csv` is in the same folder as your cleaning script.
2. Run the script using:
   python clean_sales_data.py
   

---
