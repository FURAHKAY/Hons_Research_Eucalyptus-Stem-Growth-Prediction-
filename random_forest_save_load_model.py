import joblib

# Function to save the trained model
def save_model(model, model_path):
    joblib.dump(model, model_path)
    print(f"Model saved to {model_path}.")

# Function to load the model
def load_model(model_path):
    model = joblib.load(model_path)
    print(f"Model loaded from {model_path}.")
    return model

# Example usage:
if __name__ == "__main__":
    # Load the trained model
    model = load_model('random_forest_trained_model.pkl')
    
    # Save the model
    save_model(model, 'random_forest_saved_model.pkl')
