from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import GridSearchCV
import pandas as pd
from sklearn.model_selection import train_test_split
import joblib

# Load preprocessed data
data = pd.read_csv('preprocessed_data.csv', index_col='Datetime')

# Define features and target variable
features = ['Air Temp', 'Air Hum', 'Soil Temp', 'Soil Moisture']
target = 'Dendro'

X = data[features]
y = data[target]

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Set up the hyperparameter grid
param_grid = {
    'n_estimators': [100, 200, 300],
    'max_depth': [None, 10, 20],
    'min_samples_split': [2, 5, 10],
}

# Initialize the Random Forest model
rf_model = RandomForestRegressor(random_state=42)

# Perform grid search for hyperparameter tuning
grid_search = GridSearchCV(estimator=rf_model, param_grid=param_grid, cv=5, n_jobs=-1)
grid_search.fit(X_train, y_train)

# Get the best parameters
best_params = grid_search.best_params_

# Print the best parameters and save the tuned model
print(f"Best Parameters: {best_params}")

# Save the best model
joblib.dump(grid_search.best_estimator_, 'random_forest_tuned_model.pkl')

print("Hyperparameter tuning completed and model saved.")
