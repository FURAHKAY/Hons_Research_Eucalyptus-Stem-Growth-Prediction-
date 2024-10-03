import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import tensorflow as tf
import joblib
from tensorflow.keras.models import load_model

# Load the trained neural network model
model = load_model('neural_net_trained_model.h5')

# Load the saved scaler
scaler = joblib.load('neural_net_scaler.pkl')

# Step 1: Make Predictions on New Data
# New data for prediction (real-world input data)
new_data = pd.DataFrame({
    'Air Temp': [15.2, 16.5],  # Example values for new data
    'Air Hum': [80, 85],
    'Soil Temp': [12, 12.5],
    'Soil Moisture': [20, 22]
})

# Standardize the new data
scaled_new_data = scaler.transform(new_data)

# Make predictions on the new data
new_predictions = model.predict(scaled_new_data)
print("New Data Predictions:", new_predictions)

# Step 2: Evaluate the Model on Test Data
# Load preprocessed data for evaluation
file_path = 'preprocessed_data.csv'
data = pd.read_csv(file_path, index_col='Datetime')

# Feature and target selection
features = ['Air Temp', 'Air Hum', 'Soil Temp', 'Soil Moisture']
target = 'Dendro'

X = data[features]
y = data[target]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize the test data
X_test = scaler.transform(X_test)

# Predict on the test data
y_pred = model.predict(X_test)

# Combine predictions and actual values into a DataFrame
results = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred.flatten()})

# Save the predictions to a CSV file
results.to_csv('neural_network_predictions.csv', index=False)

#print("Predictions completed and saved to 'neural_network_predictions.csv'.")
print("Predictions on test data completed and saved to 'neural_network_predictions.csv'.")

# Step 3: Print predictions from the test dataset
print("Test Data Predictions:")
print(results.head())