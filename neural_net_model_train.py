import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import EarlyStopping
from tensorflow.keras.losses import MeanSquaredError

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

# Standardize the features (mean=0, std=1)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Build the neural network model
model = Sequential([
    Dense(64, input_dim=X_train.shape[1], activation='relu'),
    Dense(32, activation='relu'),
    Dense(1, activation='linear')
])

# Compile the model with the explicit loss function class
model.compile(optimizer=Adam(learning_rate=0.001), loss=MeanSquaredError())

# Define early stopping to prevent overfitting
early_stopping = EarlyStopping(monitor='val_loss', patience=10, restore_best_weights=True)

# Neural network training with early stopping
# Train the model (assuming your training steps are already in place)
history = model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=100, batch_size=32, callbacks=[early_stopping])

# Save the model
model.save('neural_net_trained_model.h5')

# Save the scaler for future use
import joblib
joblib.dump(scaler, 'neural_net_scaler.pkl')

# Save the history to a CSV file
history_df = pd.DataFrame(history.history)
history_df.to_csv('neural_net_history.csv', index=False)
print("Model training completed and saved to 'neural_net_trained_model.h5'.")
