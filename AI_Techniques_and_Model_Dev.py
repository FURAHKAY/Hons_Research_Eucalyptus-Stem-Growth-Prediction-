# Steps:

# Describe AI Models: Explain the models you will use (e.g., linear regression, neural networks).
# Model Architecture: Detail the architecture of complex models (e.g., neural networks).
# Feature Engineering: Describe how you created and selected features.
# Training Procedures: Explain how you trained your models.
# Coding Tasks:

# Implement AI models and their architectures.
# Perform feature engineering.
# Train the models.
# AI_Model_Development.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Load and preprocess the data
dendro_data = pd.read_csv('processed_ChrisEDendroData_23Jul24.csv')
sensing_data = pd.read_csv('processed_gems_sensing_data.csv')

# Check the columns
print("Dendro Data Columns:", dendro_data.columns)
print("Sensing Data Columns:", sensing_data.columns)

# Drop any rows with missing values (if any remain)
dendro_data.dropna(inplace=True)
sensing_data.dropna(inplace=True)

# Debug: Check the size and content of the DataFrames after dropping NA values
print("Dendro Data Shape:", dendro_data.shape)
print("Sensing Data Shape:", sensing_data.shape)

# Debug: Show the first few rows of the DataFrames
print("Dendro Data Sample:\n", dendro_data.head())
print("Sensing Data Sample:\n", sensing_data.head())

# Define features and target for sensing data
sensing_data['soil_temp_diff'] = sensing_data['soil_temp_north'] - sensing_data['soil_temp_south']
sensing_features = ['Atm_pressure', 'Humidity', 'air_temp', 'solar_radiation', 'rainfall', 'soil_temp_north', 
                    'soil_temp_south', 'soil_vwc_north', 'soil_vwc_south', 'wind_speed', 'Soil_EC_BULK_north', 
                    'Soil_EC_BULK_south', 'Soil_EC_PORE_north', 'Soil_EC_PORE_south', 'Soil_Permitivity_north', 
                    'Soil_Permitivity_south', 'soil_temp_diff']
sensing_target = 'air_temp'

# Define features and target for dendro data based on available columns
dendro_features = ['field1', 'field2', 'field3', 'field4', 'field5', 'field6', 'field7']
dendro_target = 'field3'  # Example target variable

# Split data into features and labels
X_dendro = dendro_data[dendro_features]
y_dendro = dendro_data[dendro_target]

X_sensing = sensing_data[sensing_features]
y_sensing = sensing_data[sensing_target]

# Debug: Check the size and content of the feature and target DataFrames
print("X_dendro Shape:", X_dendro.shape)
print("y_dendro Shape:", y_dendro.shape)
print("X_sensing Shape:", X_sensing.shape)
print("y_sensing Shape:", y_sensing.shape)

# Split the data into training and testing sets
if X_dendro.shape[0] > 0 and y_dendro.shape[0] > 0:
    X_dendro_train, X_dendro_test, y_dendro_train, y_dendro_test = train_test_split(X_dendro, y_dendro, test_size=0.2, random_state=42)
else:
    print("No samples in dendro data to split.")

if X_sensing.shape[0] > 0 and y_sensing.shape[0] > 0:
    X_sensing_train, X_sensing_test, y_sensing_train, y_sensing_test = train_test_split(X_sensing, y_sensing, test_size=0.2, random_state=42)
else:
    print("No samples in sensing data to split.")

# Standardize the features
scaler = StandardScaler()

if X_dendro.shape[0] > 0:
    X_dendro_train_scaled = scaler.fit_transform(X_dendro_train)
    X_dendro_test_scaled = scaler.transform(X_dendro_test)
else:
    X_dendro_train_scaled, X_dendro_test_scaled = [], []

if X_sensing.shape[0] > 0:
    X_sensing_train_scaled = scaler.fit_transform(X_sensing_train)
    X_sensing_test_scaled = scaler.transform(X_sensing_test)
else:
    X_sensing_train_scaled, X_sensing_test_scaled = [], []

# Define the model
def create_model(input_dim):
    model = Sequential()
    model.add(Dense(64, input_dim=input_dim, activation='relu'))
    model.add(Dense(32, activation='relu'))
    model.add(Dense(1, activation='linear'))
    model.compile(optimizer='adam', loss='mse', metrics=['mae'])
    return model

# Train the model for dendro data if available
if len(X_dendro_train_scaled) > 0:
    dendro_model = create_model(X_dendro_train_scaled.shape[1])
    dendro_model.fit(X_dendro_train_scaled, y_dendro_train, epochs=50, batch_size=32, validation_split=0.2)

    # Evaluate the model
    dendro_loss, dendro_mae = dendro_model.evaluate(X_dendro_test_scaled, y_dendro_test)
    print(f"Dendro Model - Loss: {dendro_loss}, MAE: {dendro_mae}")
    
    # Save the model
    dendro_model.save('dendro_model.h5')
else:
    print("No training performed for dendro data due to lack of samples.")

# Train the model for sensing data if available
if len(X_sensing_train_scaled) > 0:
    sensing_model = create_model(X_sensing_train_scaled.shape[1])
    sensing_model.fit(X_sensing_train_scaled, y_sensing_train, epochs=50, batch_size=32, validation_split=0.2)

    # Evaluate the model
    sensing_loss, sensing_mae = sensing_model.evaluate(X_sensing_test_scaled, y_sensing_test)
    print(f"Sensing Model - Loss: {sensing_loss}, MAE: {sensing_mae}")
    
    # Save the model
    sensing_model.save('sensing_model.h5')
else:
    print("No training performed for sensing data due to lack of samples.")
