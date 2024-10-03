import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Load predictions and actual values from the CSV file
results = pd.read_csv('random_forest_predictions.csv')

# Plot Actual vs Predicted Values
plt.figure(figsize=(10, 6))
plt.scatter(results['Actual'], results['Predicted'], alpha=0.5)
plt.plot([results['Actual'].min(), results['Actual'].max()], 
         [results['Actual'].min(), results['Actual'].max()], 
         'r--', lw=2, label='Ideal Fit (Actual = Predicted)')
plt.xlabel('Actual Values')
plt.ylabel('Predicted Values')
plt.title('Actual vs. Predicted Values (Random Forest)')
plt.legend()
plt.grid(True)
plt.savefig('random_forest_actual_vs_predicted.png')
plt.show()

# Plot the distribution of errors
plt.figure(figsize=(10, 6))
errors = results['Actual'] - results['Predicted']
sns.histplot(errors, kde=True, bins=30, color='purple')
plt.axvline(x=0, color='r', linestyle='--', label='Ideal Error = 0')
plt.xlabel('Prediction Error (Actual - Predicted)')
plt.title('Distribution of Prediction Errors')
plt.legend()
plt.grid(True)
plt.savefig('random_forest_prediction_error_distribution.png')
plt.show()


# Correlation Analysis with Environmental Factors
corr_matrix = results.corr()
print(corr_matrix["Dendro"].sort_values(ascending=False))

# Temperature vs Tree Growth
plt.figure(figsize=(10, 6))
plt.scatter(results['Air Temp'], results['Dendro'], alpha=0.5, color='green')
plt.xlabel('Air Temperature (°C)')
plt.ylabel('Tree Diameter (mm)')
plt.title('Tree Growth vs. Air Temperature')
plt.grid(True)
plt.savefig('rf_temp_vs_tree_growth.png')  # Save the plot
plt.show()

# Soil Moisture vs Tree Growth
plt.figure(figsize=(10, 6))
plt.scatter(results['Soil Moisture'], results['Dendro'], alpha=0.5, color='blue')
plt.xlabel('Soil Moisture (%)')
plt.ylabel('Tree Diameter (mm)')
plt.title('Tree Growth vs. Soil Moisture')
plt.grid(True)
plt.savefig('rf_soil_moisture_vs_tree_growth.png')  # Save the plot
plt.show()