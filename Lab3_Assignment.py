import pandas as pd

# Sample large dataset with missing values
data = {
    'PropertyID': [1, 2, 3, 4, 5],
    'ListingDate': ['2023-01-01', '2023-02-15', '2023-03-01', '2023-04-01', '2023-05-01'],
    'SaleDate': ['2023-03-15', '2023-04-01', '2023-03-20', '2023-05-15', '2023-06-01']
}

df = pd.DataFrame(data)

# Convert Listing and SaleDate to datetime format
df['ListingDate'] = pd.to_datetime(df['ListingDate'])
df['SaleDate'] = pd.to_datetime(df['SaleDate'])

# Calculate Days on Market
df['DaysOnMarket'] = (df['SaleDate'] - df['ListingDate']).dt.days

print(df[['ListingDate', 'SaleDate', 'DaysOnMarket']])

