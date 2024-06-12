import cv2
import numpy as np
import os

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

def process_image(input_path, output_path):
    # Read the image
    image = cv2.imread(input_path)
    
    # Crop the image to the circular region with transparent background
    cropped_image = crop_to_circle(image)
    
    # Save the cropped image with transparency
    cv2.imwrite(output_path, cropped_image)

# Example usage
input_path = 'fp_scale/data/Normal/Normal_1.jpg'
output_path = 'fp_scale/data/Cropped_Normal_1.png'
process_image(input_path, output_path)

# Display the result (Optional)
import matplotlib.pyplot as plt
cropped_image = cv2.imread(output_path, cv2.IMREAD_UNCHANGED)
plt.imshow(cv2.cvtColor(cropped_image, cv2.COLOR_BGRA2RGBA))
plt.axis('off')
plt.show()
