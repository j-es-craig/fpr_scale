import os
import cv2
import numpy as np
import pandas as pd
import init

# Define the folder containing images
image_folder = init.DATA_OUT_DIR
output_csv = init.RESULTS_OUT_DIR + '/YCbCr_pixels.csv'

# Initialize the CSV file with headers
header_written = False

# Loop through each file in the image folder
for filename in os.listdir(image_folder):
    if filename.endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff')):
        # Read the image
        img_path = os.path.join(image_folder, filename)
        image = cv2.imread(img_path)

        # Convert the image to YCbCr color space
        ycbcr_image = cv2.cvtColor(image, cv2.COLOR_BGR2YCrCb)

        # Extract Y, Cr, and Cb channels
        Y, Cr, Cb = cv2.split(ycbcr_image)

        # Flatten the channels and concatenate them into a single row
        ycbcr_flat = np.hstack((Y.flatten(), Cr.flatten(), Cb.flatten()))

        # Convert the flattened array to a DataFrame
        df = pd.DataFrame([ycbcr_flat], columns=[f'Pixel_{i+1}' for i in range(len(ycbcr_flat))])
        df.insert(0, 'Image', filename)  # Insert image name at the first column

        # Append the DataFrame to the CSV file
        if not header_written:
            df.to_csv(output_csv, index=False, mode='w')
            header_written = True
        else:
            df.to_csv(output_csv, index=False, header=False, mode='a')

        print(f"Finished processing {filename}")

print(f"Data has been saved to {output_csv}")
