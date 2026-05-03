import pandas as pd


data = {'Date': ['2022-01-15', '2022-02-10', '2022-03-20', '2022-04-15', '2022-05-25'],
        'Sales': [200, 220, 250, 210, 230]}
df = pd.DataFrame(data)


df['Date'] = pd.to_datetime(df['Date'])
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month
df['DayOfWeek'] = df['Date'].dt.dayofweek
df['Quarter'] = df['Date'].dt.quarter


print("Dataset with extracted date/time features:")
print(df)