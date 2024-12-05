import cv2
import numpy as np
import matplotlib.pyplot as plt
# Load image in grayscale
img = cv2.imread("pop.jpg",cv2.IMREAD_GRAYSCALE)
# Thresholding
_, binary = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY)
# Define kernel and apply erosion
kernel = np.ones((5, 5), np.uint8)
eroded = cv2.erode(binary, kernel, iterations=1)
# Display results using subplots
plt.figure(figsize=(10, 8))
plt.subplot(121), plt.imshow(binary, cmap='gray'),
plt.title("Original Binary"), plt.axis('off')
plt.subplot(122), plt.imshow(eroded, cmap='gray'),
plt.title("Eroded"), plt.axis('off')
plt.show()
