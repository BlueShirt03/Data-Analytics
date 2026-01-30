import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer

# Sample data: Sales transactions
data = {
    'TransactionID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Store': ['A', 'B', 'A', 'C', 'B', 'A', 'C', 'B', 'A', 'C'],
    'SalesAmount': [250, 120, 340, 400, 200, np.nan, 180, 300, 220, 150],
    'Discount': [10, 15, 20, 25, 5, 12, np.nan, 18, 8, 22],
    'Date': pd.to_datetime(['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04', '2023-01-05',
                            '2023-01-06', '2023-01-07', '2023-01-08', '2023-01-09', '2023-01-10']),
    'Category': ['Electronics', 'Clothing', 'Electronics', 'Home', 'Clothing', 
                 'Home', 'Electronics', 'Home', 'Clothing', 'Electronics']
}

df = pd.DataFrame(data)

#1. Data Cleaning and Imputation
imputer = SimpleImputer(strategy='mean')
df[['SalesAmount', 'Discount']] = imputer.fit_transform(df[['SalesAmount', 'Discount']])

#2. Feature Engineering
df['DayOfWeek'] = df['Date'].dt.dayofweek
df['NetSales'] = df['SalesAmount'] - df['Discount']
df['DiscountPercentage'] = (df['Discount'] / df['SalesAmount'] * 100)

#3. Advance Filtering 
high_value_sales = df[(df['NetSales'] > 200) & (df['Store'].isin(['A', 'B']))]

#4. Aggregation and Grouping
agg_sales = df.groupby(['Store', 'Category']).agg(
    TotalSales=('NetSales', 'sum'),
    AvgSales=('NetSales', 'mean'),
    MaxDiscount=('Discount', 'max'),
    SalesCount=('TransactionID', 'count')
).reset_index()

#5. Time-based Analysis
daily_sales = df.resample('D', on='Date')['NetSales'].sum().reset_index()

#6. Data Normalization
scaler = StandardScaler()
df['NormalizedSales'] = scaler.fit_transform(df[['SalesAmount']])

# 7. Pivot Table
category_store_pivot = pd.pivot_table(df, values='NetSales', index='Category', columns='Store', aggfunc='sum', fill_value=0)

# Print results
print("Original Data:")
print(df)
print("\nHigh Value Sales:")
print(high_value_sales)
print("\nAggregated Sales:")
print(agg_sales)
print("\nDaily Sales:")
print(daily_sales)
print("\nCategory-Store Pivot:")
print(category_store_pivot)