
import numpy as np
import pandas as pd


data = {'HousePrices': [50000, 120000, 250000, 500000, 1200000, 2500000]}

df = pd.DataFrame(data)

df['LogHousePrices'] = np.log(df['HousePrices'])

print(df)