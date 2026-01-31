import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('kc_house_data.csv')

# Mean for ‘sqft_living’ column
mean_sqft_living = df['sqft_living'].mean().round(2)
#print("Mean of sqft_living:", mean_sqft_living)

# mini and max for bedrooms for houses
min_bedrooms = df['bedrooms'].min()
max_bedrooms = df['bedrooms'].max()
#print("Minimum number of bedrooms:", min_bedrooms)
#print("Maximum number of bedrooms:", max_bedrooms)

#Creating a subset homes with 2 and 4 bedrooms, and 1 and 3 bathrooms
subset_homes = df[df["bedrooms"].isin([2, 4]) & df["bathrooms"].isin([1, 3])]
#print(subset_homes)

# Finding the mean for each combination of bedrooms and bathrooms
mean_values = subset_homes.groupby(['bedrooms', 'bathrooms'])['price'].mean().round(2)
print(mean_values)

# Finding the highest count for subest_homes
combo_counts = subset_homes.groupby(['bedrooms', 'bathrooms']).size()
print(combo_counts)

# log transformation of ‘price’ column and standardize z-score
df['log_price'] = np.log(df['price'])
df['price_z'] = (df['log_price'] - df['log_price'].mean()) / df['log_price'].std()


# creating a histogram for ‘price’ column
plt.hist(df['price_z'], bins=20, edgecolor='black')
plt.title("Standardized Log Price Distribution")
plt.xlabel("Standardized Log Price")
plt.ylabel("Frequency")
plt.show()


