import cv2
import matplotlib.pyplot as plt

img = cv2.imread("pop.jpg")

lap = cv2.Laplacian(img, cv2.CV_64F)

plt.imshow(lap, cmap="gray")
plt.title("Laplacian Edge Detection")
plt.axis("off")
plt.show()