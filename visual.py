import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Load the preprocessed dataset
file_path = 'preprocessed_data.csv'  # Adjust the path if needed
data = pd.read_csv(file_path, index_col='Datetime')

# Load predictions
results_nn = pd.read_csv('neural_network_predictions.csv')  # Load NN predictions
results_rf = pd.read_csv('random_forest_predictions.csv')   # Load RF predictions

# Visualize Actual vs Predicted for Neural Network
plt.figure(figsize=(10, 6))
plt.scatter(results_nn['Actual'], results_nn['Predicted'], alpha=0.5, color='blue', label='Predicted vs Actual')
plt.plot([results_nn['Actual'].min(), results_nn['Actual'].max()], 
         [results_nn['Actual'].min(), results_nn['Actual'].max()], 
         'r--', lw=2, label='Ideal Fit (Actual = Predicted)')
plt.xlabel('Actual Values')
plt.ylabel('Predicted Values')
plt.title('Actual vs. Predicted Values (Neural Network)')
plt.legend()
plt.grid(True)
plt.savefig('nn_actual_vs_predicted.png')  # Save the plot
plt.show()

# Visualize Actual vs Predicted for Random Forest
plt.figure(figsize=(10, 6))
plt.scatter(results_rf['Actual'], results_rf['Predicted'], alpha=0.5, color='green', label='Predicted vs Actual')
plt.plot([results_rf['Actual'].min(), results_rf['Actual'].max()], 
         [results_rf['Actual'].min(), results_rf['Actual'].max()], 
         'r--', lw=2, label='Ideal Fit (Actual = Predicted)')
plt.xlabel('Actual Values')
plt.ylabel('Predicted Values')
plt.title('Actual vs. Predicted Values (Random Forest)')
plt.legend()
plt.grid(True)
plt.savefig('rf_actual_vs_predicted.png')  # Save the plot
plt.show()

# Error Distribution Plot
errors_nn = results_nn['Actual'] - results_nn['Predicted']
errors_rf = results_rf['Actual'] - results_rf['Predicted']

plt.figure(figsize=(10, 6))
sns.histplot(errors_nn, kde=True, bins=30, color='blue', label='NN Errors')
sns.histplot(errors_rf, kde=True, bins=30, color='green', label='RF Errors')
plt.axvline(x=0, color='r', linestyle='--', label='Ideal Error = 0')
plt.xlabel('Prediction Error (Actual - Predicted)')
plt.title('Distribution of Prediction Errors (NN vs RF)')
plt.legend()
plt.grid(True)
plt.savefig('error_distribution_nn_vs_rf.png')  # Save the plot
plt.show()

# Correlation Analysis with Environmental Factors
corr_matrix = data.corr()
print(corr_matrix["Dendro"].sort_values(ascending=False))

# Temperature vs Tree Growth
plt.figure(figsize=(10, 6))
plt.scatter(data['Air Temp'], data['Dendro'], alpha=0.5, color='green')
plt.xlabel('Air Temperature (°C)')
plt.ylabel('Tree Diameter (mm)')
plt.title('Tree Growth vs. Air Temperature')
plt.grid(True)
plt.savefig('tmp_temp_vs_tree_growth.png')  # Save the plot
plt.show()

# Soil Moisture vs Tree Growth
plt.figure(figsize=(10, 6))
plt.scatter(data['Soil Moisture'], data['Dendro'], alpha=0.5, color='blue')
plt.xlabel('Soil Moisture (%)')
plt.ylabel('Tree Diameter (mm)')
plt.title('Tree Growth vs. Soil Moisture')
plt.grid(True)
plt.savefig('tmp_soil_moisture_vs_tree_growth.png')  # Save the plot
plt.show()
