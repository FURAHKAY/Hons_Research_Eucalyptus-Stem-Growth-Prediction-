import tensorflow as tf
import joblib

# Function to save the model and the scaler
def save_model_and_scaler(model, scaler, model_filename='neural_net_trained_model.h5', scaler_filename='neural_net_scaler.pkl'):
    # Save the trained model
    model.save(model_filename)
    print(f"Model saved as '{model_filename}'")

    # Save the scaler for future use
    joblib.dump(scaler, scaler_filename)
    print(f"Scaler saved as '{scaler_filename}'")

# Function to load the model and the scaler
def load_model_and_scaler(model_filename='neural_net_trained_model.h5', scaler_filename='neural_net_scaler.pkl'):
    # Load the trained model
    model = tf.keras.models.load_model(model_filename)
    print(f"Model loaded from '{model_filename}'")

    # Load the scaler
    scaler = joblib.load(scaler_filename)
    print(f"Scaler loaded from '{scaler_filename}'")

    return model, scaler

if __name__ == "__main__":
    # Example usage
    # Assume `model` and `scaler` are your trained model and scaler objects

    # Save the model and scaler
    # save_model_and_scaler(model, scaler)

    # Load the model and scaler
    model, scaler = load_model_and_scaler()

