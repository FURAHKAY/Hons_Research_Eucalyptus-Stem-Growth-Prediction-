from sklearn.tree import plot_tree
import matplotlib.pyplot as plt
import joblib

# Define the features (you must ensure these match the actual feature names used in training)
features = ['Air Temp', 'Air Hum', 'Soil Temp', 'Soil Moisture']

# Load the trained Random Forest model
rf_model = joblib.load('random_forest_model.pkl')

# Plot the first decision tree in the random forest
plt.figure(figsize=(20, 10))
plot_tree(rf_model.estimators_[0], feature_names=features, filled=True, rounded=True, max_depth=3)
plt.savefig('random_forest_decision_tree.png', bbox_inches='tight')
plt.show()

# Function to save the model and scaler
def save_model_and_scaler(model, scaler, model_filename='random_forest_model.pkl', scaler_filename='random_forest_scaler.pkl'):
    # Save the trained model
    joblib.dump(model, model_filename)
    print(f"Model saved as '{model_filename}'")

    # Save the scaler for future use
    joblib.dump(scaler, scaler_filename)
    print(f"Scaler saved as '{scaler_filename}'")

# Function to load the model and scaler
def load_model_and_scaler(model_filename='random_forest_model.pkl', scaler_filename='random_forest_scaler.pkl'):
    # Load the trained model
    model = joblib.load(model_filename)
    print(f"Model loaded from '{model_filename}'")

    # Load the scaler
    scaler = joblib.load(scaler_filename)
    print(f"Scaler loaded from '{scaler_filename}'")

    return model, scaler

if __name__ == "__main__":
    # Example usage
    # Save the model and scaler
    # save_model_and_scaler(rf_model, scaler)

    # Load the model and scaler
    model, scaler = load_model_and_scaler()
