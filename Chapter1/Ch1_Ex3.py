import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Create a sample dataset
dates = pd.date_range(start='2023-01-01', periods=30, freq='D')
sales = [100, 120, np.nan, 140, 160, 150, np.nan, 200, 180, 190,
         210, 205, 215, np.nan, 230, 240, 235, 245, 250, 260,
         255, np.nan, 270, 275, 280, 285, 290, 295, 300, 310]
df = pd.DataFrame({'Date': dates, 'Sales': sales})

# Handle missing values using forward fill
df['Sales_Filled'] = df['Sales'].ffill()

# Calculate rolling averages
df['Rolling_Avg_3d'] = df['Sales_Filled'].rolling(window=3).mean()
df['Rolling_Avg_7d'] = df['Sales_Filled'].rolling(window=7).mean()
df['Rolling_Avg_14d'] = df['Sales_Filled'].rolling(window=14).mean()

# Calaculate perecent change
df['Pct_Change'] = df['Sales_Filled'].pct_change()

# Calculate cumulative sum
df['Cumulative_Sum'] = df['Sales_Filled'].cumsum()

# Display the results
print(df)

# Visualize the data
plt.figure(figsize=(12, 6))
plt.plot(df['Date'], df['Sales_Filled'], label='Filled Sales')
plt.plot(df['Date'], df['Rolling_Avg_3d'], label='3-day Rolling Average')
plt.plot(df['Date'], df['Rolling_Avg_7d'], label='7-day Rolling Average')
plt.plot(df['Date'], df['Rolling_Avg_14d'], label='14-day Rolling Average')
plt.title('Daily Sales with Rolling Averages')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()