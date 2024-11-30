import pandas as pd

# Load the dataset
file_path = 'sales_data_sample.csv'  # Replace with your dataset file path
data = pd.read_csv(file_path, encoding='ISO-8859-1')

# Preprocessing
# 1. Convert ORDERDATE to datetime format
data['ORDERDATE'] = pd.to_datetime(data['ORDERDATE'], errors='coerce')

# 2. Standardize COUNTRY names to uppercase
data['COUNTRY'] = data['COUNTRY'].str.upper()

# 3. Drop less critical columns with high missing values
columns_to_drop = ['ADDRESSLINE2', 'STATE', 'TERRITORY']
data_cleaned = data.drop(columns=columns_to_drop)

# Save the cleaned dataset to a new CSV file
cleaned_file_path = 'cleaned_sales_data.csv'
data_cleaned.to_csv(cleaned_file_path, index=False)
print(f"Preprocessed data saved to {cleaned_file_path}")