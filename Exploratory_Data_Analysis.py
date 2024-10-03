# Steps:

# Data Distributions: Analyze the distribution of key variables.
# Relationships: Explore relationships between variables.
# Visualizations: Use plots and charts to visualize your findings.
# Coding Tasks:

# Write code to generate statistical summaries.
# Create visualizations (histograms, scatter plots, correlation matrices).
# # Exploratory_Data_Analysis.py

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Define the relative paths
current_dir = os.path.dirname(__file__)
dendro_data_path = os.path.join(current_dir, 'processed_ChrisEDendroData_23Jul24.csv')
sensing_data_path = os.path.join(current_dir, 'processed_gems_sensing_data.csv')

# Load the processed datasets
dendro_data = pd.read_csv(dendro_data_path)
sensing_data = pd.read_csv(sensing_data_path)

# Function to plot histograms for each numerical column
def plot_histograms(data, columns):
    for column in columns:
        plt.figure(figsize=(14, 7))
        sns.histplot(data[column], kde=True, bins=30)
        plt.title(f'Distribution of {column}')
        plt.xlabel(column)
        plt.ylabel('Frequency')
        plt.show()

# Function to plot scatter plots for each pair of columns
def plot_scatter(data, x_columns, y_column):
    for column in x_columns:
        plt.figure(figsize=(14, 7))
        sns.scatterplot(data=data, x=column, y=y_column)
        plt.title(f'Relationship between {column} and {y_column}')
        plt.xlabel(column)
        plt.ylabel(y_column)
        plt.show()

# Function to plot box plots for each numerical column by categorical variable
def plot_box(data, x_column, y_columns):
    for column in y_columns:
        plt.figure(figsize=(14, 7))
        sns.boxplot(data=data, x=x_column, y=column)
        plt.title(f'{column} by {x_column}')
        plt.xlabel(x_column)
        plt.ylabel(column)
        plt.show()

# Data Distributions for each numerical column
numerical_columns = ['Atm_pressure', 'Humidity', 'air_temp', 'solar_radiation', 'rainfall', 'soil_temp_north', 
                     'soil_temp_south', 'soil_vwc_north', 'soil_vwc_south', 'wind_speed', 'Soil_EC_BULK_north', 
                     'Soil_EC_BULK_south', 'Soil_EC_PORE_north', 'Soil_EC_PORE_south', 'Soil_Permitivity_north', 
                     'Soil_Permitivity_south', 'soil_temp_diff']

plot_histograms(sensing_data, numerical_columns)

# Relationships between air temperature and other parameters
plot_scatter(sensing_data, numerical_columns, 'air_temp')

# Correlation Matrix
plt.figure(figsize=(14, 7))
corr_matrix = sensing_data[numerical_columns].corr()
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix of Sensing Data')
plt.show()

# Time Series Plot for each numerical column
for column in numerical_columns:
    plt.figure(figsize=(14, 7))
    sns.lineplot(data=sensing_data, x='Time', y=column)
    plt.title(f'{column} Over Time')
    plt.xlabel('Time')
    plt.ylabel(column)
    plt.show()

# Box Plot for wind speed by wind direction
plot_box(sensing_data, 'wind_direction', ['wind_speed'])

print("EDA Completed Successfully")
