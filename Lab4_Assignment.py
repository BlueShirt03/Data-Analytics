import dask.dataframe as dd
from sklearn.impute import SimpleImputer
import pandas as pd

# Sample large dataset with missing values
data = {'Age': [25, None, 22, 35, None] * 200000,
        'Salary': [50000, 60000, None, 80000, 58000] * 200000,
        'Experience': [2, 4, 1, None, 3] * 200000}

df_large = pd.DataFrame(data)

df_dask = dd.from_pandas(df_large, npartitions=10)


simple_imputer = SimpleImputer(strategy='mean')


df_dask_imputed = df_dask.map_partitions(lambda df: pd.DataFrame(simple_imputer.fit_transform(df), columns=df.columns))


df_dask_imputed = df_dask_imputed.compute()


print(df_dask_imputed.head())

