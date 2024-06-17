import os
import csv
from skimage import io
import numpy as np
import cv2
import matplotlib.pyplot as plt
import init
import logging

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Define the input and output folders
input_folder = init.DATA_OUT_DIR
output_folder = init.RESULTS_OUT_DIR
output_csv_folder = init.RESULTS_OUT_DIR
output_csv_file = os.path.join(output_csv_folder, 'dominant_colors.csv')

# Initialize CSV file if it doesn't exist
if not os.path.exists(output_csv_file):
    with open(output_csv_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['FileName', 'Y', 'Cb', 'Cr', 'Count'])

def is_black(color, threshold=30):
    """Check if the color is close to black."""
    return np.all(color < threshold)

def save_dominant_colors_to_csv(file_name, top_colors, top_counts):
    """Save the top colors and counts to the CSV file."""
    with open(output_csv_file, mode='a', newline='') as file:
        writer = csv.writer(file)
        for color, count in zip(top_colors, top_counts):
            writer.writerow([file_name] + list(color) + [count])

def plot_dominant_colors(img, top_colors, top_counts, output_file_path):
    """Plot and save the dominant colors."""
    # Convert top colors from YCbCr to RGB for plotting
    top_colors_rgb = cv2.cvtColor(np.array([top_colors], dtype=np.uint8), cv2.COLOR_YCrCb2RGB)[0]

    average = img.mean(axis=0).mean(axis=0)
    avg_patch = np.ones(shape=img.shape, dtype=np.uint8) * np.uint8(average)

    freqs = np.cumsum(np.hstack([[0], top_counts / float(top_counts.sum())]))
    rows = np.int_(img.shape[0] * freqs)

    dom_patch = np.zeros(shape=img.shape, dtype=np.uint8)
    for i in range(len(rows) - 1):
        dom_patch[rows[i]:rows[i + 1], :, :] += np.uint8(top_colors_rgb[i])

    fig, (ax0, ax1) = plt.subplots(1, 2, figsize=(12, 6))
    ax0.imshow(avg_patch)
    ax0.set_title('Average color')
    ax0.axis('off')
    ax1.imshow(dom_patch)
    ax1.set_title('Dominant colors')
    ax1.axis('off')

    plt.savefig(output_file_path)
    plt.close(fig)

def process_image(file_path, output_folder, n_colors):
    """Process an image to find and plot dominant colors."""
    try:
        # Read the image
        img = io.imread(file_path)
        if img.shape[-1] == 4:  # Remove alpha channel if present
            img = img[:, :, :-1]
        
        # Convert the image to YCbCr color space
        img_ycbcr = cv2.cvtColor(img, cv2.COLOR_RGB2YCrCb)
        pixels = np.float32(img_ycbcr.reshape(-1, 3))

        # Apply KMeans clustering to find dominant colors
        criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 200, 0.1)
        flags = cv2.KMEANS_RANDOM_CENTERS
        _, labels, palette = cv2.kmeans(pixels, n_colors, None, criteria, 10, flags)
        _, counts = np.unique(labels, return_counts=True)

        # Filter out black colors from the palette and counts
        valid_indices = [i for i, color in enumerate(palette) if not is_black(color)]
        filtered_palette = palette[valid_indices]
        filtered_counts = counts[valid_indices]

        if len(filtered_palette) == 0:
            logging.warning(f"No valid colors found in {file_path} after filtering out black.")
            return

        # Sort the colors by their count
        indices = np.argsort(filtered_counts)[::-1]
        filtered_palette = filtered_palette[indices]
        filtered_counts = filtered_counts[indices]

        # Limit to the top n dominant colors
        top_colors = filtered_palette[:n_colors]
        top_counts = filtered_counts[:n_colors]

        # Save the plot
        # output_file_path = os.path.join(output_folder, os.path.basename(file_path))
        # plot_dominant_colors(img, top_colors, top_counts, output_file_path)

        # Save the top colors and counts to the CSV file
        save_dominant_colors_to_csv(os.path.basename(file_path), top_colors , top_counts)

        logging.info(f'Processed and saved plot for {file_path}')
    except Exception as e:
        logging.error(f'Error processing {file_path}: {e}')

# Set the number of dominant colors to use
n_colors = init.N_COLORS

# Iterate over all files in the input folder
for file_name in os.listdir(input_folder):
    file_path = os.path.join(input_folder, file_name)
    if os.path.isfile(file_path):
        process_image(file_path, output_folder, n_colors)
