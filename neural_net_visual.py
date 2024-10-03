# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns

# # Load predictions and actual values from CSV
# results = pd.read_csv('neural_network_predictions.csv')

# # Plot Actual vs. Predicted Values
# plt.figure(figsize=(10, 6))
# plt.scatter(results['Actual'], results['Predicted'], alpha=0.5)
# plt.plot([results['Actual'].min(), results['Actual'].max()], [results['Actual'].min(), results['Actual'].max()], 'r--')  # Identity line
# plt.xlabel('Actual Values')
# plt.ylabel('Predicted Values')
# plt.title('Actual vs. Predicted Values')
# plt.grid(True)
# plt.show()

# # Plot Error Distribution
# plt.figure(figsize=(10, 6))
# errors = results['Actual'] - results['Predicted']
# sns.histplot(errors, kde=True, bins=30)
# plt.xlabel('Prediction Error')
# plt.title('Distribution of Prediction Errors')
# plt.grid(True)
# plt.show()

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the preprocessed dataset
file_path = 'preprocessed_data.csv'  # Adjust the path if needed
data = pd.read_csv(file_path, index_col='Datetime')
# Load predictions and actual values from CSV (replace 'neural_network_predictions.csv' with your results file)
results = pd.read_csv('neural_network_predictions.csv')  # For neural networks
# results = pd.read_csv('random_forest_predictions.csv')  # For random forest if needed

# 1. Actual vs. Predicted Values Plot
plt.figure(figsize=(10, 6))
plt.scatter(results['Actual'], results['Predicted'], alpha=0.5, color='blue', label='Predicted vs Actual')
plt.plot([results['Actual'].min(), results['Actual'].max()], 
         [results['Actual'].min(), results['Actual'].max()], 
         'r--', lw=2, label='Ideal Fit (Actual = Predicted)')
plt.xlabel('Actual Values')
plt.ylabel('Predicted Values')
plt.title('Actual vs. Predicted Values')
plt.legend()
plt.grid(True)
plt.savefig('actual_vs_predicted_plot.png')
plt.show()

# 2. Prediction Error Distribution Plot
plt.figure(figsize=(10, 6))
errors = results['Actual'] - results['Predicted']
sns.histplot(errors, kde=True, bins=30, color='purple')
plt.axvline(x=0, color='r', linestyle='--', label='Ideal Error = 0')
plt.xlabel('Prediction Error (Actual - Predicted)')
plt.title('Distribution of Prediction Errors')
plt.legend()
plt.grid(True)
plt.savefig('prediction_error_distribution.png')
plt.show()


# Correlation Analysis with Environmental Factors
# Assuming 'data' is your preprocessed dataset
corr_matrix = data.corr()
print(corr_matrix["Dendro"].sort_values(ascending=False))

# Temperature vs Tree Growth
plt.figure(figsize=(10, 6))
plt.scatter(data['Air Temp'], data['Dendro'], alpha=0.5, color='green')
plt.xlabel('Air Temperature (°C)')
plt.ylabel('Tree Diameter (mm)')
plt.title('Tree Growth vs. Air Temperature')
plt.grid(True)
plt.show()

# Soil Moisture vs Tree Growth
plt.figure(figsize=(10, 6))
plt.scatter(data['Soil Moisture'], data['Dendro'], alpha=0.5, color='blue')
plt.xlabel('Soil Moisture (%)')
plt.ylabel('Tree Diameter (mm)')
plt.title('Tree Growth vs. Soil Moisture')
plt.grid(True)
plt.show()