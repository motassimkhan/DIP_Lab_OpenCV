import cv2
import numpy as np
import matplotlib.pyplot as plt
image = cv2.imread("image.png")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray, 70, 255, cv2.THRESH_BINARY_INV)
kernel = np.ones((5, 5), np.uint8)
erosions = [cv2.erode(thresh, kernel, iterations=i) for i in range(1, 4)]
titles = ['Original Image', 'Thresholded Image', 'Erosion i=1', 'Erosion i=2', 'Erosion i=3']
images = [image, thresh] + erosions
plt.figure(figsize=(12, 8))
for i in range(5):
    plt.subplot(2, 3, i + 1)
    plt.imshow(images[i], cmap='gray')
    plt.title(titles[i])
    plt.axis('off')
plt.savefig("imageTemp.png", format="png", dpi=1200)
plt.show()
