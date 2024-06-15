import pandas as pd
import init

# Load the CSV file
file_path = init.RESULTS_OUT_DIR + '/dominant_colors.csv'
df = pd.read_csv(file_path)

# Group by FileName and aggregate the RGB values and Count
grouped_df = df.groupby('FileName').agg({'R': lambda x: list(x)[:init.N_COLORS], 
                                         'G': lambda x: list(x)[:init.N_COLORS], 
                                         'B': lambda x: list(x)[:init.N_COLORS],
                                         'Count': lambda x: list(x)[:init.N_COLORS]})

# Split the aggregated lists into separate columns
flattened_df = pd.DataFrame(grouped_df['R'].tolist(), index=grouped_df.index).add_prefix('R_').join(
               pd.DataFrame(grouped_df['G'].tolist(), index=grouped_df.index).add_prefix('G_')).join(
               pd.DataFrame(grouped_df['B'].tolist(), index=grouped_df.index).add_prefix('B_')).join(
               pd.DataFrame(grouped_df['Count'].tolist(), index=grouped_df.index).add_prefix('Count_'))

# Reset index to make 'FileName' a column
flattened_df.reset_index(inplace=True)

# Save the re-arranged dataframe to a new CSV file
output_file_path = init.RESULTS_OUT_DIR + '/rearranged.csv'
flattened_df.to_csv(output_file_path, index=False)

print(f"Re-arranged file saved to {output_file_path}")
