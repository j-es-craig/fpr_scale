import pandas as pd
import init

# Function to merge two CSV files
def merge_csv_files(file1_path, file2_path, output_path):
    # Load the two CSV files
    sheet1 = pd.read_csv(file1_path)
    sheet2 = pd.read_csv(file2_path)
    
    # Convert the file extensions in the second sheet to .png (if needed)
    sheet2['FileName'] = sheet2['FileName'].str.replace('.jpg', '.png')

    # Perform the merge operation on the FileName column
    merged_sheet = pd.merge(sheet1, sheet2, on='FileName', how='inner')

    # Remove the excess columns
    # merged_sheet = merged_sheet.drop(columns=['Unnamed: 0'])

    # Save the resulting dataframe to a new CSV file
    merged_sheet.to_csv(output_path, index=False)
    print(f"Merged file saved to: {output_path}")

# Example usage
file1_path =  init.RESULTS_OUT_DIR + '/rearranged_rgb_values.csv'
file2_path = 'fpr_scale/data/merged_zip_information.csv'
output_path = init.RESULTS_OUT_DIR + '/merged.csv'

merge_csv_files(file1_path, file2_path, output_path)
