import cv2
import matplotlib.pyplot as plt
img = cv2.imread("image.jpg")
imgrgb = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
bgr = cv2.cvtColor(imgrgb,cv2.COLOR_RGB2BGR)

images = [imgrgb,gray,bgr]
titles = ["Original", "Gray Img", "BGR Image"]
for i in range(len(images)):
    plt.subplot(1,3,i+1)
    plt.imshow(images[i])
    plt.title(titles[i])
    plt.axis('off')

plt.show()