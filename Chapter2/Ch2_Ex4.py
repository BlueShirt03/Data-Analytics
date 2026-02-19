import pandas as pd
import numpy as np
import time

# Create a large dataset
n_rows = 1000000
df = pd.DataFrame({
    'id': range(n_rows),
    'category': np.random.choice(['A', 'B', 'C'], n_rows),
    'value': np.random.randn(n_rows)
})


# Function to perform a complex operation
def complex_operation(x):
    return np.sin(x) * np.cos(x) + np.tan(x)

# Measure time without filtering
start_time = time.time()
result_without_filter = df['value'].apply(complex_operation).sum()
time_without_filter = time.time() - start_time

# Apply complex filter
filtered_df = df[(df['category'] == 'A') & (df['value'] > 0)]

# Measure time with filtering
start_time = time.time()
result_with_filter = filtered_df['value'].apply(complex_operation).sum()
time_with_filter = time.time() - start_time

print(f"Time without filtering: {time_without_filter:.2f} seconds")
print(f"Time with filtering: {time_with_filter:.2f} seconds")
print(f"Speed improvement: {time_without_filter / time_with_filter:.2f}x")