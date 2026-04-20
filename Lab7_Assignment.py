from sklearn.preprocessing import PolynomialFeatures
import pandas as pd

data = {'Age': [25, 30, 35, 40, 45]}

df = pd.DataFrame(data)

poly = PolynomialFeatures( degree=3, include_bias=False)

polynomial_features = poly.fit_transform(df[['Age']])

df_poly = pd.DataFrame(polynomial_features, columns=['Age', 'Age^2', 'Age^3'])

print(df_poly)
