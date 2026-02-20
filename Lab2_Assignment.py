from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd
import numpy as np


# Sample data: Customer transactions
data = {'CustomerID': [1, 2, 3, 4, 5],
        'PurchaseAmount': [250, np.nan, 300, 400, np.nan],
        'Discount': [10, 15, 20, np.nan, 5]}

df = pd.DataFrame(data)

# Solution
# Step 1: Define features and target
df['HighValue'] = (df['PurchaseAmount'] > 300).astype(int)
X = df[['PurchaseAmount', 'Discount']]
y = df['HighValue']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)


# Step 2: Create the pipeline
pipeline = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='mean')),  # Impute missing values
    ('scaler', StandardScaler()),  # Scale features
    ('classifier', RandomForestClassifier(random_state=42))  # Train Random Forest model
])

# Step 3: Train the pipeline
pipeline.fit(X_train, y_train)
Pipeline(steps=[(('imputer', SimpleImputer()), ('scaler', StandardScaler()), ('classifier', RandomForestClassifier(random_state=42)))])


# Step 4: Make predictions and evaluate the model
y_pred = pipeline.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print(f"Y test results are \n{y_test}\n")
print(f"Y prediction test is {y_pred}\n")
print(f"The accurcay from the test is {accuracy}\n")
