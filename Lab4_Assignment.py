import dask.dataframe as dd
from sklearn.impute import SimpleImputer
import pandas as pd

# Sample large dataset with missing values
data = {'Age': [25, None, 22, 35, None] * 200000,
        'Salary': [50000, 60000, None, 80000, 58000] * 200000,
        'Experience': [2, 4, 1, None, 3] * 200000}

df_large = pd.DataFrame(data)

# Convert the Pandas dataframe to a Dask dataframe
df_dask = dd.from_pandas(df_large, npartitions=10)

# Define a SimpleImputer
simple_imputer = SimpleImputer(strategy='mean')

# Apply the imputer on the Dask dataframe
df_dask_imputed = df_dask.map_partitions(lambda df: pd.DataFrame(simple_imputer.fit_transform(df), columns=df.columns))

# Compute the result
df_dask_imputed = df_dask_imputed.compute()

# View the first few rows of the imputed dataframe
print(df_dask_imputed.head())

