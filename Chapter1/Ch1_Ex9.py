import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

# Sample sales data
data = {
    'SalesAmount': [100, 150, 200, 250, 300, 350, 400, 450, 500, 1000],
    'ProductCategory': ['A', 'B', 'A', 'C', 'B', 'A', 'C', 'B', 'A', 'C']
}
df = pd.DataFrame(data)

# Convert SalesAmount column to Numpy array 
sales_np = df['SalesAmount'].to_numpy()

# Apply logarithmic transformation to reduce skewness
log_sales = np.log(sales_np)

# Calculate basic statistics
mean_sales = np.mean(sales_np)
meidan_sales = np.median(sales_np)
std_sales = np.std(sales_np)

# Calculate z-scores
z_scores = stats.zscore(sales_np)

# Identify outliers (z-score > 3 or < -3)
outliers = np.abs(z_scores) > 3

# Print results
print("Original Sales:", sales_np)
print("Log-transformed Sales:", log_sales)
print("Mean Sales:", mean_sales)
print("Median Sales:", meidan_sales)
print("Standard Deviation:", std_sales)
print("Z-scores:", z_scores)
print("Outliers:", df[outliers])

# Visualize the data
plt.figure(figsize=(12, 6))

plt.subplot(121)
plt.hist(sales_np, bins=10, edgecolor='black')
plt.title('Original Sales Distribution')
plt.xlabel('Sales Amount')
plt.ylabel('Frequency')

plt.subplot(122)
plt.hist(log_sales, bins=10, edgecolor='black')
plt.title('Log-transformed Sales Distribution')
plt.xlabel('Log(Sales Amount)')
plt.ylabel('Frequency')

plt.tight_layout()
plt.show()