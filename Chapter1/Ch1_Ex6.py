import pandas as pd 
# Sample data with more details
data = {'Store': ['A', 'B', 'A', 'B', 'A', 'B'],
        'Sales': [200, 220, 210, 250, 215, 240],
        'Category': ['Electronics', 'Clothing', 'Electronics', 
                     'Clothing', 'Electronics', 'Clothing']}

df = pd.DataFrame(data)
# Group by Store and Category, calculating multiple aggregations
agg_sales = df.groupby(['Store', 'Category']).agg(avg_sales=('Sales', 'mean'), totale_sales=('Sales', 'sum')).reset_index()

print(agg_sales)