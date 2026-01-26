import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Sample data: Daily sales for a retail store
data = {
    'Date': pd.date_range(start='2023-01-01', periods=30, freq='D'),
    'Sales': [200, 220, np.nan, 250, 260, 240, np.nan, 300, 280, 290,
              310, 305, 315, np.nan, 330, 340, 335, 345, 350, 360,
              355, np.nan, 370, 375, 380, 385, 390, 395, 400, 410],
    'Category': ['A', 'B', 'A', 'C', 'B', 'A', 'C', 'B', 'A', 'C',
                 'A', 'B', 'C', 'A', 'B', 'C', 'A', 'B', 'C', 'A',
                 'B', 'C', 'A', 'B', 'C', 'A', 'B', 'C', 'A', 'B']
}

df = pd.DataFrame(data)

# Display the first few rows of the dataframe
print("Original DataFrame:")
print(df.head())

# Basic statistics of the Sales column
print("\nBasic Statistics of Sales:")
print(df['Sales'].describe())

# Handling missing values
df['Sales_Filled'] = df['Sales'].ffill()

# Calculate rolling average
df['Rolling_Avg_7d'] = df['Sales_Filled'].rolling(window=7).mean()

#Group by Category and calculate mean sales
category_avg = df.groupby('Category')['Sales_Filled'].mean()
print("\nAverage Sales by Category:")
print(category_avg)

# Optimized data types
df['Sales'] = pd.to_numeric(df['Sales'], downcast='float')
df['Sales_Filled'] = pd.to_numeric(df['Sales_Filled'], downcast='float')
df['Rolling_Avg_7d'] = pd.to_numeric(df['Rolling_Avg_7d'], downcast='float')

print("\nMemory Usage After Optimization:")
print(df.memory_usage(deep=True))

# Visualization the data 
plt.figure(figsize=(12, 6))
plt.plot(df['Date'], df['Sales_Filled'], label='Sales (Filled)')
plt.plot(df['Date'], df['Rolling_Avg_7d'], label='7-day Rolling Average')
plt.title('Daily Sales and 7-day Rolling Average')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

