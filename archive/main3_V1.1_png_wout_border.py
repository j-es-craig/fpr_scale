import os
import csv
from skimage import io
import numpy as np
import cv2
import matplotlib.pyplot as plt

# Define the input and output folders
input_folder = 'fp_scale/data/post_processed/Normal/'
output_folder = 'fp_scale/results/post_processed/Normal/'
output_csv_folder = 'fp_scale/results/post_processed/Normal'
output_csv_file = os.path.join(output_csv_folder, 'dominant_colors.csv')

if not os.path.exists(output_csv_file):
    with open(output_csv_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['FileName', 'R', 'G', 'B', 'Count'])

def process_image(file_path, output_folder, n_colors=5):
    # Read the image
    img = io.imread(file_path)[:,:,:-1]
    average = img.mean(axis=0).mean(axis=0) # calculate mean value of RGB channels across image
    pixels = np.float32(img.reshape(-1, 3)) # reshape matrix

    n_colors = 4 # set colors, ensure to adjust this in other scripts
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 200, .1)
    flags = cv2.KMEANS_RANDOM_CENTERS

    _, labels, palette = cv2.kmeans(pixels, n_colors, None, criteria, 10, flags)
    _, counts = np.unique(labels, return_counts=True)

    dominant = palette[np.argmax(counts)]

    avg_patch = np.ones(shape=img.shape, dtype=np.uint8)*np.uint8(average)

    indices = np.argsort(counts)[::-1]   
    freqs = np.cumsum(np.hstack([[0], counts[indices]/float(counts.sum())]))
    rows = np.int_(img.shape[0]*freqs)

    dom_patch = np.zeros(shape=img.shape, dtype=np.uint8)
    for i in range(len(rows) - 1):
        dom_patch[rows[i]:rows[i + 1], :, :] += np.uint8(palette[indices[i]])

    # plot the dominant colors    
    fig, (ax0, ax1) = plt.subplots(1, 2, figsize=(12,6))
    ax0.imshow(avg_patch)
    ax0.set_title('Average color')
    ax0.axis('off')
    ax1.imshow(dom_patch)
    ax1.set_title('Dominant colors')
    ax1.axis('off')

    # Save the plot
    output_file_path = os.path.join(output_folder, os.path.basename(file_path) + '_dominant_colors.png')
    plt.savefig(output_file_path)
    plt.close(fig)

    # Save the palette and counts to the CSV file, modify in excel
    with open(output_csv_file, mode='a', newline='') as file:
        writer = csv.writer(file)
        for color, count in zip(palette, counts):
            writer.writerow([os.path.basename(file_path)] + list(color) + [count])

# Iterate over all files in the input folder
for file_name in os.listdir(input_folder):
    file_path = os.path.join(input_folder, file_name)
    if os.path.isfile(file_path):
        try:
            process_image(file_path, output_folder)
            print(f'Processed and saved plot for {file_name}')
        except Exception as e:
            print(f'Error processing {file_name}: {e}')
