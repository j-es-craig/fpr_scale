import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('fpr_scale/results/post_processed/Normal/cleaned_data_with_hex_colors.csv')

# Select relevant columns for analysis
columns_to_exclude = ['eye', 'Gender', 'Gestational age at birth(week)', 'Gestational age at birth(day)', 'Birth weight(g)', 'Hex Color']
data_for_analysis = data.drop(columns=columns_to_exclude)

# Normalize the data
scaler = StandardScaler()
scaled_data = scaler.fit_transform(data_for_analysis)

# Perform PCA
pca = PCA(n_components=2)
pca_result = pca.fit_transform(scaled_data)

# Perform K-means clustering with 4 clusters
optimal_clusters = 4
kmeans = KMeans(n_clusters=optimal_clusters, random_state=42)
clusters = kmeans.fit_predict(pca_result)

# Add the cluster labels and hex color to the PCA result dataframe
pca_result_df = pd.DataFrame(pca_result, columns=['PC1', 'PC2'])
pca_result_df['Cluster'] = clusters
pca_result_df['Hex Color'] = data['Hex Color']

# Plot the PCA result with hex color and discrete cluster legend
plt.figure(figsize=(10, 7))

# Plot each cluster separately with corresponding hex color
for cluster in range(optimal_clusters):
    clustered_data = pca_result_df[pca_result_df['Cluster'] == cluster]
    plt.scatter(clustered_data['PC1'], clustered_data['PC2'], color=clustered_data['Hex Color'], label=f'Cluster {cluster}', alpha=0.6)

plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.title('PCA Result by Dominant Hex Code')
plt.show()
