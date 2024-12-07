import cv2
import matplotlib.pyplot as plt


img = cv2.imread("img.jpg")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

lap1 = cv2.Laplacian(gray,cv2.CV_64F)
ret,thresh = cv2.threshold(lap1, 20,255,cv2.THRESH_BINARY_INV)

denoise = cv2.GaussianBlur(gray,(3,3),0)
lap2 = cv2.Laplacian(denoise,cv2.CV_64F)
ret,thresh2 = cv2.threshold(lap2,20,255,cv2.THRESH_BINARY_INV)

images = [gray, lap1, thresh, denoise, lap2, thresh2]
titles = ['gray img', 'laplacian Edging', 'Inverse thresholding', 'Denoise Image', 'Edging on denoise image','Inverse thresholding']

for i in range(len(images)):
    plt.subplot(3, 3, i+1)
    plt.imshow(images[i],cmap='gray')
    plt.title(titles[i])
    plt.axis('off')
    
plt.show()