import pandas as pd


data = {'Name': ['Alice', 'Bob', 'Charlie', 'Diana'],
        'Age': [25, 132, 30, -5]}
df = pd.DataFrame(data)

out_of_range = df[(df['Age'] < 0) | (df['Age'] > 120)]


df = df[(df['Age'] >= 0) & (df['Age'] <= 120)]


print("Out-of-range values:")
print(out_of_range)

print("\nDataset after removing out-of-range values:")
print(df)