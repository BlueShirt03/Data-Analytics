import dask.dataframe as dd
from sklearn.impute import SimpleImputer
import pandas as pd

# Sample large dataset with missing values
data = {'Age': [25, None, 22, 35, None] * 200000,
        'Salary': [50000, 60000, None, 80000, 58000] * 200000,
        'Experience': [2, 4, 1, None, 3] * 200000}

df_large = pd.DataFrame(data)