import cv2
import numpy as np
import os

def crop_to_circle(image):
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Apply a binary threshold to get a binary image
    _, binary = cv2.threshold(gray, 20, 255, cv2.THRESH_BINARY)
    
    # Find contours in the binary image
    contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Get the largest contour
    largest_contour = max(contours, key=cv2.contourArea)
    
    # Create a mask from the largest contour
    mask = np.zeros_like(image)
    cv2.drawContours(mask, [largest_contour], -1, (255, 255, 255), thickness=cv2.FILLED)
    
    # Apply the mask to the image
    result = cv2.bitwise_and(image, mask)
    
    # Crop the image to the bounding rectangle of the largest contour
    x, y, w, h = cv2.boundingRect(largest_contour)
    cropped_image = result[y:y+h, x:x+w]
    
    return cropped_image

def process_images(input_path, output_path):
    # Read the image
    image = cv2.imread(input_path)
    
    # Crop the image to the circular region
    cropped_image = crop_to_circle(image)
    
    # Save the cropped image
    cv2.imwrite(output_path, cropped_image)

# Example usage
input_path = 'fp_scale/data/Normal/Normal_1.jpg'
output_path = 'fp_scale/data/Cropped_Normal_1.jpg'
process_images(input_path, output_path)

# Display the result (Optional)
import matplotlib.pyplot as plt
cropped_image = cv2.imread(output_path)
plt.imshow(cv2.cvtColor(cropped_image, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.show()
