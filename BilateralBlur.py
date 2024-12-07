import cv2
import matplotlib.pyplot as plt

img = cv2.imread("img.jpg")
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

bil5 = cv2.bilateralFilter(img,5,75,75)
bil15 = cv2.bilateralFilter(img,15,100,100)

images = [img,bil5,bil15]
titles=['Original',"bilateral d = 5", "Bilateral d = 15"]

for i in range(len(images)):
    plt.subplot(1,3,i+1)
    plt.imshow(images[i])
    plt.title(titles[i])
    plt.axis('off')

plt.show()