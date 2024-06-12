import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the clustered Excel file
file_path = 'fp_scale/results/clustered_output.xlsx'
data = pd.read_excel(file_path)

# Select RGB columns
rgb_columns = [col for col in data.columns if col.startswith(('R_', 'G_', 'B_'))]

# Calculate the mean RGB values for each cluster
mean_rgb_by_cluster = data.groupby('Cluster')[rgb_columns].mean()

# Plot the mean RGB values for each cluster
plt.figure(figsize=(12, 8))
mean_rgb_by_cluster.plot(kind='bar')
plt.title('Mean RGB Values by Cluster')
plt.xlabel('Cluster')
plt.ylabel('Mean RGB Value')
plt.legend(loc='upper right', bbox_to_anchor=(1.15, 1))
plt.show()

# Save the mean RGB values by cluster to a new Excel file
output_file_path = 'fp_scale/results/mean_rgb_by_cluster.xlsx'
mean_rgb_by_cluster.to_excel(output_file_path, index=True)

print(f"Mean RGB values by cluster saved to {output_file_path}")
