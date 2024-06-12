import cv2
import numpy as np
import os

def crop(image, threshold=20):
    y_nonzero, x_nonzero, _ = np.nonzero(image > threshold)
    return image[np.min(y_nonzero):np.max(y_nonzero), np.min(x_nonzero):np.max(x_nonzero)]

def process_images(input_folder, output_folder, threshold=20):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.endswith('.jpg'):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)
            
            # Read the image
            image = cv2.imread(input_path)
            
            # Crop the dark gray border
            cropped_image = crop(image, threshold)
            
            # Save the cropped image
            cv2.imwrite(output_path, cropped_image)

# Example usage
input_folder = 'fp_scale/data/Normal'
output_folder = 'fp_scale/data/post_processed/Normal'
process_images(input_folder, output_folder)
