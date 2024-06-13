import pandas as pd

# Load the dataset
file_path = 'path_to_your_file/merged_data.csv'
data = pd.read_csv(file_path)

# Recode the 'eye' and 'Gender' columns
data['eye'] = data['eye'].map({'OD': 0, 'OS': 1})
data['Gender'] = data['Gender'].map({'Male': 0, 'Female': 1})

# Remove the specified columns
data_cleaned = data.drop(columns=['Unnamed: 0', 'ID'])

# Display the first few rows of the cleaned dataset
print(data_cleaned.head())

# Optionally, save the cleaned dataset to a new CSV file
data_cleaned.to_csv('path_to_your_file/cleaned_data.csv', index=False)

