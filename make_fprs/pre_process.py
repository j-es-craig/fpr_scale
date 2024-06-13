import cv2
import numpy as np
import os
import init

def crop_to_circle(image):
    # Convert to grayscale to find contours
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Apply a binary threshold to get a binary image
    _, binary = cv2.threshold(gray, 20, 255, cv2.THRESH_BINARY)
    
    # Find contours in the binary image
    contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Get the largest contour
    largest_contour = max(contours, key=cv2.contourArea)
    
    # Get the center and radius of the minimum enclosing circle around the largest contour
    (x, y), radius = cv2.minEnclosingCircle(largest_contour)
    center = (int(x), int(y))
    radius = int(radius)
    
    # Create a mask with the same dimensions as the image
    mask = np.zeros(image.shape[:2], dtype=np.uint8)
    
    # Draw a filled circle on the mask
    cv2.circle(mask, center, radius, 255, thickness=-1)
    
    # Create a 4-channel image (BGR + Alpha)
    result = cv2.cvtColor(image, cv2.COLOR_BGR2BGRA)
    
    # Set the alpha channel based on the mask
    result[:, :, 3] = mask
    
    # Crop the image to the bounding box of the circle
    x, y, w, h = cv2.boundingRect(largest_contour)
    cropped_image = result[y:y+h, x:x+w]
    
    return cropped_image

def process_images(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, os.path.splitext(filename)[0] + '.png')
            
            # Read the image
            image = cv2.imread(input_path)
            
            # Crop the image to the circular region with transparent background
            cropped_image = crop_to_circle(image)
            
            # Save the cropped image with transparency
            cv2.imwrite(output_path, cropped_image)

# set filepaths and execute
input_folder = init.DATA_DIR
output_folder = init.DATA_OUT_DIR
process_images(input_folder, output_folder)