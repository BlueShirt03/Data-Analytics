import pandas as pd

# Sample data
data = {'Store': ['A', 'B', 'A', 'B', 'A', 'B'],
        'Sales': [200, 220, 210, 250, 215, 240]}

df = pd.DataFrame(data)

#Group by 'Store' and calculate average sales
average_sales = df.groupby('Store')['Sales'].mean()
print(average_sales)
