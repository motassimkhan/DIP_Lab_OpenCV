import cv2
import matplotlib.pyplot as plt

img = cv2.imread("image1.png")
imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
Bil_Img5 = cv2.bilateralFilter(imgRGB, 5, 75, 75)
k5_blur = cv2.blur(imgRGB, (5, 5))

plt.subplot(131), plt.imshow(imgRGB), plt.title('Original Image'), plt.axis('off')
plt.subplot(132), plt.imshow(Bil_Img5), plt.title('Bilateral Blur d=5'), plt.axis('off')
plt.subplot(133), plt.imshow(k5_blur), plt.title('Box Blur k=5'), plt.axis('off')
plt.show()
