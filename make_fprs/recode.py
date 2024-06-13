import pandas as pd
import init
import os

# Load the dataset
file_path = init.RESULTS_OUT_DIR + '/merged.csv'
data = pd.read_csv(file_path)

# Recode the 'eye' and 'Gender' columns
data['eye'] = data['eye'].map({'OD': 0, 'OS': 1})
data['Gender'] = data['Gender'].map({'Male': 0, 'Female': 1})

# Remove the specified columns
data_cleaned = data.drop(columns=['ID'])

# Display the first few rows of the cleaned dataset
print(data_cleaned.head())

# Optionally, save the cleaned dataset to a new CSV file
data_cleaned.to_csv(init.RESULTS_OUT_DIR + '/cleaned.csv', index=False)

