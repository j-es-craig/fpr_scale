import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Load the Excel file
file_path = 'fp_scale/results/modified_output.xlsx'
data = pd.read_excel(file_path)

# Drop non-numeric columns and other 
# numeric_data = data.select_dtypes(include=['float64', 'int64'])
columns_to_exclude = ['eye', 'Gender', 'Birth weight(g)', 'Gestational age (weeks)']
numeric_data = data.drop(columns=columns_to_exclude + ['FileName', 'ID'])

# Standardize the data
scaler = StandardScaler()
scaled_data = scaler.fit_transform(numeric_data)

# Perform PCA
pca = PCA(n_components=2)
pca_result = pca.fit_transform(scaled_data)

# Add PCA results to the dataframe
data['PCA1'] = pca_result[:, 0]
data['PCA2'] = pca_result[:, 1]

# Perform K-means clustering
kmeans = KMeans(n_clusters=3, random_state=42)
clusters = kmeans.fit_predict(scaled_data)

# Add cluster labels to the dataframe
data['Cluster'] = clusters

# Save the modified data with PCA and cluster labels
output_file_path = 'fp_scale/results/clustered_output.xlsx'
data.to_excel(output_file_path, index=False)

# Plot the PCA result
plt.figure(figsize=(10, 7))
plt.scatter(data['PCA1'], data['PCA2'], c=data['Cluster'], cmap='viridis')
plt.xlabel('PCA1')
plt.ylabel('PCA2')
plt.title('PCA of the Dataset')
plt.colorbar(label='Cluster')
plt.show()

print(f"Modified file with PCA and clustering saved to {output_file_path}")
