import cv2
import numpy as np
import matplotlib.pyplot as plt

################## Prepare Images ######################

img = cv2.imread('HarryPotter.jpg', 0)

################## Edge Detection ######################

# Laplacian
lap = cv2.Laplacian(img, cv2.CV_64F, ksize=3)
lap = np.uint8(np.absolute(lap))

# SobelX
sobelX = cv2.Sobel(img, cv2.CV_64F, 1, 0)
sobelX = np.uint8(np.absolute(sobelX))

# SobelY
sobelY = cv2.Sobel(img, cv2.CV_64F, 0, 1)
sobelY = np.uint8(np.absolute(sobelY))

# Sobel combined
sobelCombined = cv2.bitwise_or(sobelX, sobelY)

# Canny
canny = cv2.Canny(img, 100, 75)

################## Show images ########################

images = [img, lap, sobelX, sobelY, sobelCombined, canny]
titles = ['Original', 'Laplacian', 'Sobel X', 'Sobel Y', 'Sobel combined', 'Canny']

n_images = len(images)
row = (n_images-1)//3 + 1
col = 3

fig, ax = plt.subplots(row, col)
for i, image in enumerate(images):
    if row == 1:
        ax[i%3].imshow(image, 'gray')
        ax[i%3].axes.xaxis.set_visible(False)
        ax[i%3].axes.yaxis.set_visible(False)
        ax[i%3].axes.set_title(titles[i], fontsize=10)
    else:
        ax[i//3, i%3].imshow(image, 'gray')
        ax[i//3, i%3].axes.xaxis.set_visible(False)
        ax[i//3, i%3].axes.yaxis.set_visible(False)
        ax[i//3, i%3].axes.set_title(titles[i], fontsize=10)

white_img = np.zeros((120, 120, 3), np.uint8)
white_img[:] = 255
if i < row * col - 1:
    for j in range(i+1, row * col):
        if row == 1:
            ax[j % 3].imshow(white_img, 'gray')
            ax[j % 3].axes.xaxis.set_visible(False)
            ax[j % 3].axes.yaxis.set_visible(False)
        else:
            ax[j // 3, j % 3].imshow(white_img, 'gray')
            ax[j // 3, j % 3].axes.xaxis.set_visible(False)
            ax[j // 3, j % 3].axes.yaxis.set_visible(False)

plt.show()


