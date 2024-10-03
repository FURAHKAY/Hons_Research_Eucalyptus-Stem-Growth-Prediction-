import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import StandardScaler

def preprocess_data(file_path, save_path):
    # Load data with the correct delimiter (semicolon)
    data = pd.read_csv(file_path, delimiter=';')
    
    # Print the column names to debug
    print(data.columns)  # This will help you identify the exact column names
    
    # Define the numeric columns
    numeric_columns = ['Dendro', 'Air Temp', 'Air Hum', 'Soil Temp', 'Soil Moisture', 'Battery Level']
    
    for column in numeric_columns:
        # Convert column to string before applying string operations
        data[column] = data[column].astype(str)
        
        # Step 1: Remove periods that are used as thousand separators
        data[column] = data[column].str.replace(r'\.', '', regex=True)
        
        # Step 2: Replace commas with periods for decimal points
        data[column] = data[column].str.replace(',', '.', regex=False)
        
        # Step 3: Convert to float
        try:
            data[column] = data[column].astype(float)
        except ValueError as e:
            print(f"Conversion error in column {column}: {e}")
    
    # Combine Date and Time into a single Datetime column
    data['Datetime'] = pd.to_datetime(data['Date'] + ' ' + data['Time'])
    data.set_index('Datetime', inplace=True)
    data.drop(['Date', 'Time'], axis=1, inplace=True)
    
    # Handle missing values (forward fill)
    data.ffill(inplace=True)
    
    # 1. Removing Duplicates
    data.drop_duplicates(inplace=True)
    
    # 2. Handling Outliers
    # You can define limits based on your domain knowledge
    for column in ['Air Temp', 'Air Hum', 'Soil Temp', 'Soil Moisture']:
        upper_limit = data[column].mean() + 3 * data[column].std()  # Set upper limit (3 standard deviations)
        lower_limit = data[column].mean() - 3 * data[column].std()  # Set lower limit
        data[column] = np.where(data[column] > upper_limit, upper_limit, data[column])  # Cap upper outliers
        data[column] = np.where(data[column] < lower_limit, lower_limit, data[column])  # Cap lower outliers
    
    # 3. Handling Missing Data with Imputation Algorithm
    def impute_missing_values(data, window=2):
        """
        Impute missing values by using the median change from surrounding nodes.
        data: DataFrame containing time series data.
        window: Number of surrounding data points to consider for imputation.
        """
    # Iterate over each column in the list of time series columns
    # The missing value is filled by adding the median change (calculated from the surrounding values) 
    # to the previous value in the column
    for column in ['Air Temp', 'Air Hum', 'Soil Temp', 'Soil Moisture', 'Dendro']:
        # Iterate over each row in the DataFrame
        for i in range(len(data)):
            # Check if the current value in the column is NaN (missing)
            if pd.isna(data[column].iloc[i]):
                # Get the surrounding values within the window range, drop any NaNs
                surrounding_values = data[column].iloc[max(0, i-window):i+window].dropna()
                
                # If there are more than one valid surrounding values
                if len(surrounding_values) > 1:
                    # Calculate the median of the differences (changes) between consecutive values
                    median_change = np.median(np.diff(surrounding_values))
                    
                    # Impute the missing value by adding the median change to the previous value
                    data.at[i, column] = data[column].iloc[i-1] + median_change
        # Return the DataFrame with imputed values
        return data

    # Save the data before imputation for visualization purposes
    data_before = data.copy()

    # Apply imputation algorithm to fill missing values
    data_after = impute_missing_values(data_before.copy())
    # Check missing values before imputation
    print("Missing values before imputation:")
    print(data_before.isna().sum())

    # After imputation, check the difference
    print("Missing values after imputation:")
    print(data_after.isna().sum())


    # Visualization of missing data before and after imputation
    missing_before = data_before.isna().sum() / len(data_before) * 100
    print("Missing percentage before imputation:")
    print(missing_before)

    missing_after = data_after.isna().sum() / len(data_after) * 100
    print("Missing percentage after imputation:")
    print(missing_after)


   # Ensure there is missing data to visualize
    if missing_before.sum() == 0:
        print("No missing data to plot.")
    else:
        # Bar plot for missing values before and after imputation
        plt.figure(figsize=(10, 6))
        plt.bar(missing_before.index, missing_before.values, alpha=0.6, label="Before Imputation", color='blue')
        plt.bar(missing_after.index, missing_after.values, alpha=0.6, label="After Imputation", color='green')
        plt.xlabel("Features")
        plt.ylabel("Percentage of Missing Values")
        plt.title("Missing Data Before and After Imputation")
        plt.legend()
        plt.grid(True)
        plt.savefig('missing_data_imputation.png')  # Save the figure
        plt.show()

    # Scatter plot for a feature before and after imputation (e.g., 'Air Temp')
    if 'Air Temp' in data_before.columns and 'Air Temp' in data_after.columns:
        plt.figure(figsize=(10, 6))
        plt.scatter(data_before['Air Temp'], data_after['Air Temp'], alpha=0.5, color='blue', label='Air Temp: Before vs After')
        plt.plot([data_before['Air Temp'].min(), data_before['Air Temp'].max()], 
                 [data_before['Air Temp'].min(), data_before['Air Temp'].max()], 
                 'r--', lw=2, label='Ideal Fit (Before = After)')
        plt.xlabel('Air Temp (Before)')
        plt.ylabel('Air Temp (After)')
        plt.title('Air Temperature: Before vs After Imputation')
        plt.legend()
        plt.grid(True)
        plt.savefig('air_temp_before_after_imputation.png')  # Save the figure
        plt.show()
    else:
        print("'Air Temp' column is missing.")

    # 4. Scaling the Features
    features = ['Air Temp', 'Air Hum', 'Soil Temp', 'Soil Moisture']
    scaler = StandardScaler()
    data_after[features] = scaler.fit_transform(data_after[features])

    # Save the preprocessed data after imputation and scaling
    data_after.to_csv(save_path, index=True)

    # Feature and target selection
    X = data_after[features]
    y = data_after['Dendro']

    print(f"Data Preprocessing Completed! Saved to {save_path}")
    print(data_after.head())  # Print the first few rows of the preprocessed data
    print(data_after.dtypes)  # Print the data types to verify numeric columns
        
    return X, y, data_after

if __name__ == "__main__":
    file_path = 'eucalyptus_data.csv'  # Replace with your actual file path
    save_path = 'preprocessed_data.csv'  # Path to save the preprocessed data
    X, y, data = preprocess_data(file_path, save_path)
    
    print(f"Data Preprocessing Completed! Saved to {save_path}")
    print("Features (X):")
    print(X.head())  # Print the first few rows of the features
    print("Target (y):")
    print(y.head())  # Print the first few rows of the target variable

