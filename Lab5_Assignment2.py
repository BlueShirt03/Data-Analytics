from sklearn.preprocessing import PowerTransformer
import pandas as pd

data = {'Profit': [-5000, -2000, 0, 3000, 15000]}

df = pd.DataFrame(data)

yeojohnson_transformer = PowerTransformer(method='yeo-johnson')
df['YeoJohnsonProfit'] = yeojohnson_transformer.fit_transform(df[['Profit']])


print(df)