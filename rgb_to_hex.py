import pandas as pd

# Load your data
data = pd.read_csv('fpr_scale/results/post_processed/Normal/cleaned_data.csv')

# Function to convert RGB values to HEX color
def rgb_to_hex(r, g, b):
    return f'#{int(r):02X}{int(g):02X}{int(b):02X}'

# Apply the function to create a new column
data['Hex Color'] = data.apply(lambda row: rgb_to_hex(row['R_0'], row['G_0'], row['B_0']), axis=1)

# Save the updated dataframe with the hex color column to a new CSV file
output_file_path = 'fpr_scale/results/post_processed/Normal/cleaned_data_with_hex_colors.csv'
data.to_csv(output_file_path, index=False)
