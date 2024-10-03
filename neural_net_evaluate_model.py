import pandas as pd
import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
import tensorflow as tf
import joblib

# Load preprocessed data
file_path = 'preprocessed_data.csv'
data = pd.read_csv(file_path, index_col='Datetime')

# Feature and target selection
features = ['Air Temp', 'Air Hum', 'Soil Temp', 'Soil Moisture']
target = 'Dendro'

X = data[features]
y = data[target]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Load the trained model and scaler
model = tf.keras.models.load_model('neural_net_trained_model.h5')
scaler = joblib.load('neural_net_scaler.pkl')

# Standardize the test data
X_test = scaler.transform(X_test)

# Predict on the test data
y_pred = model.predict(X_test)

# Evaluate the model
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Print performance metrics
print(f"Mean Absolute Error (MAE): {mae}")
print(f"Mean Squared Error (MSE): {mse}")
print(f"R² Score: {r2}")

# Save performance metrics to a text file
with open('neural_net_model_evaluation.txt', 'w') as f:
    f.write(f"Mean Absolute Error (MAE): {mae}\n")
    f.write(f"Mean Squared Error (MSE): {mse}\n")
    f.write(f"R² Score: {r2}\n")

print("Model evaluation completed and saved to 'neural_net_model_evaluation.txt'.")

