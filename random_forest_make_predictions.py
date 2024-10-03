import pandas as pd
import joblib

# Load preprocessed data
file_path = 'preprocessed_data.csv'
data = pd.read_csv(file_path, index_col='Datetime')

# Feature selection
features = ['Air Temp', 'Air Hum', 'Soil Temp', 'Soil Moisture']
X = data[features]
y_actual = data['Dendro']  # Actual target values

# Load the trained model and scaler
model = joblib.load('random_forest_model.pkl')
scaler = joblib.load('random_forest_scaler.pkl')

# Standardize the data
X_scaled = scaler.transform(X)

# Make predictions
predictions = model.predict(X_scaled)

# Save predictions and actual values to a CSV file
results_df = pd.DataFrame({'Actual': y_actual, 'Predicted': predictions}, index=data.index)
results_df.to_csv('random_forest_predictions.csv')

print("Predictions saved to 'random_forest_predictions.csv'.")
