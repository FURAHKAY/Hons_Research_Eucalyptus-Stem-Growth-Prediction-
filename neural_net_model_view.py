from tensorflow.keras.utils import plot_model 
import tensorflow as tf
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Load the neural network model
model = tf.keras.models.load_model('neural_net_trained_model.h5')

# Print the model architecture
model.summary()

# Save the model architecture as a PNG file
plot_model(model, to_file='neural_net_model_architecture.png', show_shapes=True, show_layer_names=True)
print("Model architecture saved as 'neural_net_model_architecture.png'.")

# Load the history from the CSV file (assuming you saved it during training)
history_file = 'neural_net_history.csv'  # Replace with your actual history file path
history = pd.read_csv(history_file)

# Plot training & validation loss values
plt.figure(figsize=(10, 6))
plt.plot(history['loss'], label='Training Loss')
plt.plot(history['val_loss'], label='Validation Loss')
plt.title('Model Loss Over Epochs')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend(['Train', 'Validation'], loc='upper right')
plt.grid(True)
# Save the training loss and validation loss plot as a PNG file
plt.savefig('neural_net_loss_curve.png')
plt.show()
print("Loss curve saved as 'neural_net_loss_curve.png'.")

# Save training and validation loss values to a CSV file
history.to_csv('neural_net_loss_data.csv', index=False)
print("Training and validation loss values saved to 'neural_net_loss_data.csv'.")

# Get weights and biases
for layer in model.layers:
    weights = layer.get_weights()
    print(f"Weights for layer {layer.name}: {weights}")

# Save the model summary to a text file
with open('neural_net_model_summary.txt', 'w') as f:
    model.summary(print_fn=lambda x: f.write(x + '\n'))
print("Model summary saved to 'neural_net_model_summary.txt'.")

# Save weights and biases of each layer to a file
with open('neural_net_model_weights.txt', 'w') as f:
    for layer in model.layers:
        weights = layer.get_weights()
        f.write(f"Weights for layer {layer.name}: {weights}\n")
print("Model weights and biases saved to 'neural_net_model_weights.txt'.")
