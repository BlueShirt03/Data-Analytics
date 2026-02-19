import pandas as pd
import numpy as np

# Sample data
data = {
    'OrderID': [1001, 1002, 1003, 1004, 1005],
    'CustomerID': ['C001', 'C002', 'C003', 'C004', 'C005'],
    'OrderDate': ['2023-01-15', '2023-01-16', '2023-01-17', '2023-01-18', '2023-01-19'],
    'TotalAmount': [100.50, 200.75, -50.00, 1000000.00, 150.25],
    'Status': ['Completed', 'Pending', 'Completed', 'Shipped', 'Invalid']
}

df = pd.DataFrame(data)

# Convert OrderDate to datetime
df['OrderDate'] = pd.to_datetime(df['OrderDate'])

# Identify and filter out orders with negative or unusually high amounts
valid_orders = df[(df['TotalAmount']> 0) & (df['TotalAmount'] < 100000)]

#Identify and filter out oders with invalid status
invalid_status = df[~df['Status'].isin(['Completed', 'Pending', 'Shipped'])]


print("Valid Orders:")
print(valid_orders)
print("\nOrders with Invalid Status:")  
print(invalid_status)

# Clean the data be remoiving invalid entries and resetting the index 
cleaned_df = df[(df['TotalAmount']> 0) & (df['TotalAmount'] < 100000) & (df['Status'].isin(['Completed', 'Pending', 'Shipped']))].reset_index(drop=True)

print("\nCleaned DataFrame:")
print(cleaned_df)  