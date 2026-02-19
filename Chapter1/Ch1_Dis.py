import pandas as pd

df = pd.read_csv('kc_house_data.csv')

summary_stats = df['price'].describe().to_frame("Price Stats").round(2)
print(summary_stats)