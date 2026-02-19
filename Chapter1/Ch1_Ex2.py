import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Create a sample dataset
dates = pd.date_range(start='2023-01-01', periods=30, freq='D')
sales = [100, 120, np.nan, 140, 160, 150, np.nan, 200, 180, 190,
         210, 205, 215, np.nan, 230, 240, 235, 245, 250, 260,
         255, np.nan, 270, 275, 280, 285, 290, 295, 300, 310]
categories = ['A', 'B', 'A', 'C', 'B', 'A', 'C', 'B', 'A', 'C',
              'A', 'B', 'C', 'A', 'B', 'C', 'A', 'B', 'C', 'A',
              'B', 'C', 'A', 'B', 'C', 'A', 'B', 'C', 'A', 'B']

df = pd.DataFrame({'Date': dates, 'Sales': sales, 'Category': categories})

# Display initial information
print("Original DataFrame:")
print(df.head())
print("\n DataFrame Info:")
print(df.info())

# Handle missing values by forward filling
df['Sales_Filled'] = df['Sales'].ffill()

# Calculate various rolling average
df['Rolling_Avg_3d'] = df['Sales_Filled'].rolling(window=3).mean()
df['Rolling_Avg_7d'] = df['Sales_Filled'].rolling(window=7).mean()

# Group by Category and calculate total sales
category_stats = df.groupby('Category')['Sales_Filled'].agg(['mean', 'median', 'std'])
print("\nSales Statistics by Category:")
print(category_stats)

# Optimize data types
df['Sales'] = pd.to_numeric(df['Sales'], downcast='float')
df['Sales_Filled'] = pd.to_numeric(df['Sales_Filled'], downcast='float')
df['Rolling_Avg_3d'] = pd.to_numeric(df['Rolling_Avg_3d'], downcast='float')
df['Rolling_Avg_7d'] = pd.to_numeric(df['Rolling_Avg_7d'], downcast='float')
print("\nMemory Usage After Optimization:")
print(df.memory_usage(deep=True))

# Visualize the data
plt.figure(figsize=(12, 6))
plt.plot(df['Date'], df['Sales'], label='Original Sales', alpha=0.7)
plt.plot(df['Date'], df['Sales_Filled'], label='Filled Sales')
plt.plot(df['Date'], df['Rolling_Avg_3d'], label='3-day Rolling Average')
plt.plot(df['Date'], df['Rolling_Avg_7d'], label='7-day Rolling Average')
plt.title('Daily Sales with Rolling Averages')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Print final DataFrame
print("\nFinal DataFrame:")
print(df)