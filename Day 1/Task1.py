import pandas as pd

# Load the dataset
df = pd.read_csv("sales_data.csv")
print(df)

# Find Null Value
print(df.isnull().sum())

# Remove rows with duplicate value
df = df.dropna()
print(df)

df.drop_duplicates()
print(df)

# Clean Text Format
df['Payment Method'] = df['Payment Method'].str.strip().str.title()

# Convert the data types

df['Date'] = pd.to_datetime(df['Date'])
df['Quantity'] = df['Quantity'].astype(int)
df['Price'] = df['Price'].astype(float)
df['Total'] = df['Total'].astype(float)

# Recalculate the Total Column
df['Total'] = df['Quantity'] * df['Price']

# Save cleaned dataset
df.to_csv("sales_data_cleaned.csv", index=False)