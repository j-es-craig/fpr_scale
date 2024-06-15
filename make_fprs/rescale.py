import pandas as pd
import init

# Load the dataset
file_path = init.RESULTS_OUT_DIR + '/rearranged.csv'
data = pd.read_csv(file_path)

# Extract columns
count_columns = [col for col in data.columns if 'Count' in col]
r_columns = [col for col in data.columns if 'R_' in col]
g_columns = [col for col in data.columns if 'G_' in col]
b_columns = [col for col in data.columns if 'B_' in col]

# Calculate total sum of 'Count' columns for each row
data['Total_Count'] = data[count_columns].sum(axis=1)

# Calculate the percentage of each 'Count' column
for count_col in count_columns:
    data[count_col + '_Percent'] = data[count_col] / data['Total_Count']

# Scale R, G, and B columns by their respective 'Count' percentages
for i in range(len(r_columns)):
    r_col = r_columns[i]
    g_col = g_columns[i]
    b_col = b_columns[i]
    count_percent_col = count_columns[i] + '_Percent'
    
    data[r_col + '_Scaled'] = data[r_col] * data[count_percent_col]
    data[g_col + '_Scaled'] = data[g_col] * data[count_percent_col]
    data[b_col + '_Scaled'] = data[b_col] * data[count_percent_col]

# Extract only the scaled RGB columns along with the FileName
scaled_columns = [col for col in data.columns if 'Scaled' in col]
scaled_data = data[['FileName'] + scaled_columns]

# Save the processed dataset to a new CSV file
output_file_path = init.RESULTS_OUT_DIR + '/rescaled.csv'
scaled_data.to_csv(output_file_path, index=False)
