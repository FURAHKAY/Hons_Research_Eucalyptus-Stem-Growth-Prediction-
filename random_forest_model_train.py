import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score  # Add these imports


# Function to train the model
def train_model(X, y, train_save_path, test_save_path):
    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Save the training and testing sets to new files
    X_train.to_csv(f'{train_save_path}_X_train.csv', index=True)
    X_test.to_csv(f'{test_save_path}_X_test.csv', index=True)
    y_train.to_csv(f'{train_save_path}_y_train.csv', index=True)
    y_test.to_csv(f'{test_save_path}_y_test.csv', index=True)
    
    # Standardize the features (mean=0, std=1)
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    # Train the model (Random Forest Regressor)
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train_scaled, y_train)
    
    # Save the trained model and scaler to a file
    joblib.dump(model, 'random_forest_model.pkl')
    joblib.dump(scaler, 'random_forest_scaler.pkl')  # Save the scaler for future use
    
    return X_test_scaled, y_test, model

# Function to evaluate the model
def evaluate_model(model, X_test, y_test):
    # Make predictions
    y_pred = model.predict(X_test)
    
    # Calculate performance metrics
    mae = mean_absolute_error(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    
    print("Model Performance:")
    print(f"Mean Absolute Error (MAE): {mae}")
    print(f"Mean Squared Error (MSE): {mse}")
    print(f"R² Score: {r2}")
    
    return y_pred

if __name__ == "__main__":
    # Load preprocessed data
    data_path = 'preprocessed_data.csv'  # Path to the preprocessed data
    data = pd.read_csv(data_path, index_col=0)
    
    # Define features and target
    features = ['Air Temp', 'Air Hum', 'Soil Temp', 'Soil Moisture']  # Modify features as needed
    target = 'Dendro'
    
    X = data[features]
    y = data[target]
    
    # Paths to save train/test data
    train_save_path = 'random_forest_train_data'
    test_save_path = 'random_forest_test_data'
    
    # Train the model
    X_test, y_test, model = train_model(X, y, train_save_path, test_save_path)
    
    # Evaluate the model
    y_pred = evaluate_model(model, X_test, y_test)

    print("Model training and evaluation completed!")
