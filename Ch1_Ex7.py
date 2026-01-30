import pandas as pd
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer

# Sample data with missing values
data = {
    'Feature1': [1, 2, np.nan, 4, 5],
    'Feature2': [10, np.nan, 12, 14, 15],
    'Category': ['A', 'B', 'A', 'C', 'B']
}

df = pd.DataFrame(data)

# Define processing for numerical columns
numeric_features = ['Feature1', 'Feature2']
numeric_transformer = Pipeline(steps=[('imputer', SimpleImputer(strategy='mean')),('scaler', StandardScaler())])

# Define processing for categorial columns
categorical_features = ['Category']
categorical_transformer = Pipeline(steps=[('imputer', SimpleImputer(strategy='constant', fill_value='missing')), ('onehot', OneHotEncoder(handle_unknown='ignore'))])

# Combine preprocessing steps 
preprocessor = ColumnTransformer(transformers=[('num', numeric_transformer, numeric_features), ('cat', categorical_transformer, categorical_features)])

# Create and fit the pipeline
pipeline = Pipeline(steps=[('preprocessor', preprocessor)])
transformed_data = pipeline.fit_transform(df)

# Convert to DataFrame for better visualization
feature_names = (numeric_features + pipeline.named_steps['preprocessor'].named_transformers_['cat'].named_steps['onehot'].get_feature_names_out(categorical_features).tolist())


transformed_df = pd.DataFrame(transformed_data, columns=feature_names)

print("Original Data:")
print(df)
print("\nTransformed Data:")
print(transformed_df)
