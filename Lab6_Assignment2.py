import pandas as pd

# Sample data with high cardinality
data = {'ProductCategory': ['Electronics', 'Furniture', 'Electronics', 'Clothing', 'Furniture', 'Clothing', 'Electronics']}

df = pd.DataFrame(data)

df['ProductCategory_Frequency'] = df.groupby('ProductCategory')['ProductCategory'].transform('count')

print(df)