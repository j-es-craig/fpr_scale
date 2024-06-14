import pandas as pd

# Define the path to your CSV files. Adjust the pattern to match your filenames.
csv_files = []

# Initialize an empty list to store the dataframes
dataframes = []

# Iterate over the list of files and read each into a dataframe
for file in csv_files:
    df = pd.read_csv(file)
    dataframes.append(df)

# Concatenate all dataframes vertically
concatenated_df = pd.concat(dataframes, ignore_index=True)

# Save the concatenated dataframe to a new CSV file
concatenated_df.to_csv('fpr_scale/results/concatenated_file.csv', index=False)
