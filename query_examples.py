import pandas as pd

# Load the cleaned data
data = pd.read_csv('cleaned_sales_data.csv')

# Example Queries
# 1. Total orders by year
total_orders_by_year = data.groupby('YEAR_ID')['ORDERNUMBER'].nunique()

# 2. Customer with the most orders
most_orders_customer = data.groupby('CUSTOMERNAME')['ORDERNUMBER'].nunique().idxmax()

# 3. Top 5 customers by total sales
top_5_customers = data.groupby('CUSTOMERNAME')['SALES'].sum().nlargest(5)

# 4. Product line with the most sales
top_product_line = data.groupby('PRODUCTLINE')['SALES'].sum().idxmax()

# 5. Sales distribution by country
sales_by_country = data.groupby('COUNTRY')['SALES'].sum()

# 6. Number of orders shipped vs. those in dispute or canceled
order_status_counts = data['STATUS'].value_counts()

# 7. Orders placed each month in a given year (e.g., 2023)
orders_per_month_2023 = data[data['YEAR_ID'] == 2023].groupby('MONTH_ID')['ORDERNUMBER'].nunique()

# 8. Country with the highest number of customers
top_country_by_customers = data.groupby('COUNTRY')['CUSTOMERNAME'].nunique().idxmax()

# Print results
print("Total Orders by Year:\n", total_orders_by_year)
print("Customer with Most Orders:", most_orders_customer)
print("Top 5 Customers by Sales:\n", top_5_customers)
print("Top Product Line by Sales:", top_product_line)
print("Sales by Country:\n", sales_by_country)
print("Order Status Counts:\n", order_status_counts)
print("Orders Per Month in 2023:\n", orders_per_month_2023)
print("Country with Most Customers:", top_country_by_customers)