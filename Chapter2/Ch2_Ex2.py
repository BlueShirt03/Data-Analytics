import pandas as pd
import numpy as np

# Sample data
data = {
    'CustomerID': ['C001', 'C002', 'C003', 'C004', 'C005', 'C001', 'C002', 'C003'],
    'Age': [25, 35, 45, 30, 50, 25, 35, 45],
    'Gender': ['M', 'F', 'M', 'F', 'M', 'M', 'F', 'M'],
    'ProductCategory': ['Electronics', 'Clothing', 'Home', 'Beauty', 'Sports', 'Clothing', 'Electronics', 'Beauty'],
    'PurchaseAmount': [500, 150, 300, 200, 450, 200, 600, 100]
}

df = pd.DataFrame(data)

# Targeted analysis: Female customers aged 30-40 who made purchases in Electronics or Clothing
target_segment = df[(df['Gender'] == 'F') & (df['Age'].between(30,40)) & (df['ProductCategory'].isin(['Electronics', 'Clothing']))]

# Calculate average purchase amount for the target segment
avg_purchase = target_segment['PurchaseAmount'].mean()

# Find the most popular product category in the target segment
popular_castegory = target_segment['ProductCategory'].mode().values[0]

print("Target Segment Analysis:")
print(f"Average Purchase Amount: ${avg_purchase:.2f}")
print(f"Most Popular Category: {popular_castegory}")

# Compare with overall average
overall_avg = df['PurchaseAmount'].mean()
print(f"\nOverall Average Purchase Amount: ${overall_avg:.2f}")
print(f"Difference: ${avg_purchase - overall_avg:.2f}")