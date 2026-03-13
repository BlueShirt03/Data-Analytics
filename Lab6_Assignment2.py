import pandas as pd

# Sample data
data = {'Neighborhood': ['A', 'B', 'A', 'C', 'B'],
        'SalePrice': [300000, 450000, 350000, 500000, 470000]}

df = pd.DataFrame(data)

neighborhood_mean = df.groupby('Neighborhood')['SalePrice'].mean()

df['NeighborhoodEncoded'] = df['Neighborhood'].map(neighborhood_mean)

print(df[['Neighborhood', 'SalePrice', 'NeighborhoodEncoded']])