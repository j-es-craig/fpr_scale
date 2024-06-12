import os
import csv
from skimage import io
import numpy as np
import cv2

# Define the input and output folders
input_folder = 'fp_scale/data/Normal/'
output_folder = 'fp_scale/results/Normal/'
output_csv_folder = 'fp_scale/results/'
output_csv_file = os.path.join(output_csv_folder, 'dominant_colors.csv')

def process_image(file_path, output_folder, n_colors=5):
    # Read the image
    img = io.imread(file_path)[:,:,:]
    average = img.mean(axis=0).mean(axis=0) # calculate mean value of RGB channels across image
    pixels = np.float32(img.reshape(-1, 3)) # reshape matrix

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

    # Prepare the CSV row data
    row_data = [os.path.basename(file_path)]
    for i in range(n_colors):
        if i < len(palette):
            color = palette[indices[i]]
            count = counts[indices[i]]
            row_data.extend(color.astype(int).tolist() + [int(count)])
        else:
            # Add placeholders for missing colors
            row_data.extend([None, None, None, None])

    # Save the palette and counts to the CSV file
    with open(output_csv_file, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(row_data)

# Write the header to the CSV file
n_colors = 5
header = ['FileName']
for i in range(n_colors):
    header.extend([f'R{i+1}', f'G{i+1}', f'B{i+1}', f'Count{i+1}'])

with open(output_csv_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(header)

# Iterate over all files in the input folder
for file_name in os.listdir(input_folder):
    file_path = os.path.join(input_folder, file_name)
    if os.path.isfile(file_path):
        try:
            process_image(file_path, output_folder)
            print(f'Processed and saved data for {file_name}')
        except Exception as e:
            print(f'Error processing {file_name}: {e}')
