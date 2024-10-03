# Steps:

# Describe Data Sources: Outline where and how you obtained your data.
# Data Collection Procedures: Detail the steps taken to collect the data.
# Data Cleaning: Explain how you handled missing values, outliers, etc.
# Preprocessing: Describe any data transformations, scaling, encoding, etc.
# Coding Tasks:

# Write code for loading and inspecting the data.
# Implement data cleaning procedures (handling missing values, outliers).
# Perform data preprocessing (scaling, encoding categorical variables).
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
import os

# Define the relative paths
current_dir = os.path.dirname(__file__)
dendro_data_path = os.path.join(current_dir, 'ChrisEDendroData_23Jul24.csv')
sensing_data_path = os.path.join(current_dir, 'gems_sensing_data.csv')

# Load the datasets
dendro_data = pd.read_csv(dendro_data_path)
sensing_data = pd.read_csv(sensing_data_path)

# Convert date columns to datetime
dendro_data['created_at'] = pd.to_datetime(dendro_data['created_at'], errors='coerce')
sensing_data['Time'] = pd.to_datetime(sensing_data['Time'], errors='coerce')

# Check for duplicates and remove them
dendro_data.drop_duplicates(inplace=True)
sensing_data.drop_duplicates(inplace=True)

# Handle missing values by filling with the mean for numerical columns
# dendro_data = dendro_data.apply(lambda x: x.fillna(x.mean()) if x.dtype.kind in 'biufc' else x)
# sensing_data = sensing_data.apply(lambda x: x.fillna(x.mean()) if x.dtype.kind in 'biufc' else x)
for column in dendro_data.select_dtypes(include=[np.number]).columns:
    dendro_data[column].fillna(dendro_data[column].mean(), inplace=True)

for column in sensing_data.select_dtypes(include=[np.number]).columns:
    sensing_data[column].fillna(sensing_data[column].mean(), inplace=True)


# Identify and remove outliers using Z-score method
# z_scores_dendro = np.abs((dendro_data.select_dtypes(include=[np.number]) - dendro_data.select_dtypes(include=[np.number]).mean()) / dendro_data.select_dtypes(include=[np.number]).std())
# dendro_data = dendro_data[(z_scores_dendro < 3).all(axis=1)]

# z_scores_sensing = np.abs((sensing_data.select_dtypes(include=[np.number]) - sensing_data.select_dtypes(include=[np.number]).mean()) / sensing_data.select_dtypes(include=[np.number]).std())
# sensing_data = sensing_data[(z_scores_sensing < 3).all(axis=1)]

# Feature Engineering: Example of creating a new feature (difference in soil temperature)
sensing_data['soil_temp_diff'] = sensing_data['soil_temp_north'] - sensing_data['soil_temp_south']

# Define the scaler
scaler = StandardScaler()

# Scale numerical features
dendro_data_numerical = dendro_data.select_dtypes(include=[np.number])
# Verify that there are still numerical columns left for scaling
if not dendro_data_numerical.empty:
    dendro_data_scaled = scaler.fit_transform(dendro_data_numerical)
    dendro_data_scaled = pd.DataFrame(dendro_data_scaled, columns=dendro_data_numerical.columns)
    dendro_data_scaled['created_at'] = dendro_data['created_at'].values
else:
    print("Warning: No numerical data left in dendro_data for scaling.")
    dendro_data_scaled = dendro_data.copy()

sensing_data_numerical = sensing_data.select_dtypes(include=[np.number])
if not sensing_data_numerical.empty:
    sensing_data_scaled = scaler.fit_transform(sensing_data_numerical)
    sensing_data_scaled = pd.DataFrame(sensing_data_scaled, columns=sensing_data_numerical.columns)
    sensing_data_scaled['Time'] = sensing_data['Time'].values
else:
    print("Warning: No numerical data left in sensing_data for scaling.")
    sensing_data_scaled = sensing_data.copy()

# Display the first few rows of the cleaned and preprocessed data
print("Dendro Data Scaled:")
print(dendro_data_scaled.head())

print("\nSensing Data Scaled:")
print(sensing_data_scaled.head())
# Save the processed data to new CSV files
dendro_data_scaled.to_csv(os.path.join(current_dir, 'processed_ChrisEDendroData_23Jul24.csv'), index=False)
sensing_data_scaled.to_csv(os.path.join(current_dir, 'processed_gems_sensing_data.csv'), index=False)

print("Data Preparation Completed Successfully")