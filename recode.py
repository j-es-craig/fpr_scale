import pandas as pd

# Load the Excel file
file_path = 'path_to_your_file/merged_output.xlsx'
data = pd.read_excel(file_path, sheet_name='Sheet1')

# Recode Eye Side: OD = 0, OS = 1
data['eye'] = data['eye'].map({'OD': 0, 'OS': 1})

# Recode Gender: Male = 0, Female = 1
data['Gender'] = data['Gender'].map({'Male': 0, 'Female': 1})

# Create a new column for gestational age in weeks
data['Gestational age (weeks)'] = data['Gestational age at birth(week)'] + (data['Gestational age at birth(day)'] / 7)

# Drop the old week and day columns
data = data.drop(columns=['Gestational age at birth(week)', 'Gestational age at birth(day)'])

# Save the modified data to a new Excel file
output_file_path = 'path_to_save_your_file/modified_output.xlsx'
data.to_excel(output_file_path, index=False)

print(f"Modified file saved to {output_file_path}")
