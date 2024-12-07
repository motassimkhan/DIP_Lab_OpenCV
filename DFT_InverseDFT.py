import cv2
import numpy as np

image = cv2.imread("image.jpg", cv2.IMREAD_GRAYSCALE)
fourier = cv2.dft(np.float32(image), flags=cv2.DFT_COMPLEX_OUTPUT)

magnitude = np.fft.fftshift(np.log(cv2.magnitude(fourier[:, :, 0], fourier[:, :, 1]) + 1))
idft_magnitude = cv2.magnitude(*cv2.split(cv2.idft(fourier)))  # Inverse DFT and magnitude

cv2.imshow("Original Image", image)
cv2.imshow("Magnitude Spectrum", np.uint8(cv2.normalize(magnitude, None, 0, 255, cv2.NORM_MINMAX)))
cv2.imshow("Reconstructed Image from Inverse DFT", np.uint8(cv2.normalize(idft_magnitude, None, 0, 255, cv2.NORM_MINMAX)))

cv2.waitKey(0)
cv2.destroyAllWindows()
