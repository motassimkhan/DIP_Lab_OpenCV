import cv2
import matplotlib.pyplot as plt

# Load and process the image
img_path = "img.jpg"  # Specify the correct file path
img = cv2.imread(img_path)
if img is None:
    raise FileNotFoundError(f"Image not found at {img_path}")

# Convert to RGB and then to grayscale
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)

# Apply Adaptive Thresholding
# Syntax: cv2.adaptiveThreshold(source, maxValue, adaptive method, type Threshold, Blocksize, Constant)
adaptive_thresh_mean = cv2.adaptiveThreshold(
    img_gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2
)
adaptive_thresh_gaussian = cv2.adaptiveThreshold(
    img_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 15, 3
)
adaptive_thresh_mean_large = cv2.adaptiveThreshold(
    img_gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 21, 10
)

# Display results
plt.figure(figsize=(10, 8))
plt.subplot(221), plt.imshow(img_gray, cmap='gray'), plt.title("Original Image"), plt.axis("off")
plt.subplot(222), plt.imshow(adaptive_thresh_mean), plt.title("Adaptive Mean"), plt.axis("off")
plt.subplot(223), plt.imshow(adaptive_thresh_gaussian), plt.title("Adaptive Gaussian"), plt.axis("off")
plt.subplot(224), plt.imshow(adaptive_thresh_mean_large), plt.title("Adaptive Mean (Large)"), plt.axis("off")
plt.tight_layout()
plt.show()