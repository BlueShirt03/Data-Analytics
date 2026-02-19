import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Create a sample dataset
dates = pd.date_range(start='2023-01-01', periods=30, freq='D')
sales = [100, 120, np.nan, 140, 160, 150, np.nan, 200, 180, 190,
         210, 205, 215, np.nan, 230, 240, 235, 245, 250, 260,
         255, np.nan, 270, 275, 280, 285, 290, 295, 300, 310]
categories = ['A', 'B', 'C'] * 10
df = pd.DataFrame({'Date': dates, 'Sales': sales, 'Category': categories})

# Display initial information
print("Original DataFrame:")
print(df.head())
print("\n intial Memory Usage:")
print(df.memory_usage(deep=True))

# Handle missing values by forward filling
df['Sales_Filled'] = df['Sales'].ffill()

# Optimize data types
df['Sales'] = pd.to_numeric(df['Sales'], downcast='float')
df['Sales_Filled'] = pd.to_numeric(df['Sales_Filled'], downcast='float')
df['Category'] = df['Category'].astype('category')

# Calculate various metrics
df['Rolling_Avg_3d'] = df['Sales_Filled'].rolling(window=3).mean()
df['Rolling_Avg_7d'] = df['Sales_Filled'].rolling(window=7).mean()
df['Pct_Change'] = df['Sales_Filled'].pct_change()
df['Cumulative_Sum'] = df['Sales_Filled'].cumsum()

# Calculate Category-wise statistics
category_stats = df.groupby('Category')['Sales_Filled'].agg(['mean', 'median', 'std'])
print("\nCategory_stats:")
print(category_stats) 

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
print(df.head())