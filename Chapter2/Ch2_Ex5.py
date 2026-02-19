import pandas as pd
import numpy as np

# Create a more comprehensive sample dataset
np.random.seed(42)
data = {
    'TransactionID': range(1001, 1021),
    'Store': np.random.choice(['A', 'B', 'C'], 20),
    'SalesAmount': np.random.randint(50, 500, 20),
    'Discount': np.random.randint(0, 30, 20),
    'Category': np.random.choice(['Electronics', 'Clothing', 'Home', 'Food'], 20),
    'Date': pd.date_range(start='2023-01-01', periods=20)
}

df = pd.DataFrame(data)

# Display the original dataset
print("Original Dataset:")
print(df)
print("\n")

# Filtering with multiple conditions
filtered_df = df[
    (df['Store'] == 'A') & 
    (df['SalesAmount'] > 200) & 
    (df['Discount'] <= 10) &
    (df['Category'].isin(['Electronics', 'Clothing']))
]

print("Filtered Dataset:")
print(filtered_df)
print("\n")


# Additional analysis on the filtered data
print("Summary Statistics of Filtered Data:")
print(filtered_df.describe())
print("\n")

print("Average Sales Amount by Category:")
print(filtered_df.groupby('Category')['SalesAmount'].mean())
print("\n")

print("Total Sales Amount by Date:")
print(filtered_df.groupby('Date')['SalesAmount'].sum())


