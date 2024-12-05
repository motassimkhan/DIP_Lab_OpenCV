import cv2
import matplotlib.pyplot as plt

img = cv2.imread("image.png")
imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

thresholds = [
    (cv2.THRESH_BINARY, 'Binary Threshold'),
    (cv2.THRESH_BINARY_INV, 'Binary Threshold Inverted'),
    (cv2.THRESH_TRUNC, 'Truncated Threshold'),
    (cv2.THRESH_TOZERO, 'Set to 0'),
    (cv2.THRESH_TOZERO_INV, 'Set to 0 Inverted')
]

threshold_images = []
titles = []

for t, title in thresholds:
    ret, thresh = cv2.threshold(gray, 120, 255, t)
    threshold_images.append(thresh)
    titles.append(title)

plt.subplot(3, 3, 1), plt.imshow(imgRGB), plt.title('Original Image'), plt.axis('off')
plt.subplot(3, 3, 2), plt.imshow(gray, cmap='gray'), plt.title('Grayscale Image'), plt.axis('off')

for i in range(5):
    plt.subplot(3, 3, i+3), plt.imshow(threshold_images[i], cmap='gray'), plt.title(titles[i]), plt.axis('off')

plt.show()
