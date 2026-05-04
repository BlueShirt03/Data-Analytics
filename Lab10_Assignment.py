import pandas as pd


data = {'Feature1': [1, 2, 3, 4, 5],
        'Feature2': [2, 4, 6, 8, 10],  
        'Feature3': [5, 3, 6, 2, 1],
        'Feature4': [10, 12, 15, 20, 25]}
df = pd.DataFrame(data)

correlation_matrix = df.corr()
threshold = 0.8
corr_features = set()

for i in range(len(correlation_matrix.columns)):
    for j in range(i):
        if abs(correlation_matrix.iloc[i,j]) > threshold:
            colname = correlation_matrix.columns[i]
            corr_features.add(colname)

df_reduced = df.drop(columns=corr_features)

print("Reduced dataset with correlated features removed:")
print(df_reduced)
