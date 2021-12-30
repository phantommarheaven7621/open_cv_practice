import cv2
import numpy as np
import matplotlib.pyplot as plt

################## Prepare Images ######################

img = cv2.imread('doreamon.jpg', cv2.IMREAD_GRAYSCALE)
img = img[199:615, 564:930]
imgBlur = cv2.GaussianBlur(img, (7, 7), 0)
imgCanny = cv2.Canny(img, 150, 200)
#_, img = cv2.threshold(img, 150, 255, cv2.THRESH_BINARY)

################## Morphological Transformation ######################

kernel = np.ones((2, 2), np.uint8)
imgDilation = cv2.dilate(imgCanny, kernel, iterations=1)
imgErosion = cv2.erode(imgDilation, kernel, iterations=1)
imgOpening = cv2.morphologyEx(imgDilation, cv2.MORPH_OPEN, kernel) # Erode + Dilate
imgClosing = cv2.morphologyEx(imgCanny, cv2.MORPH_CLOSE, kernel) # Dilate + Erode
imgGradient = cv2.morphologyEx(imgCanny, cv2.MORPH_GRADIENT, kernel) # Morph gradient
imgTophat = cv2.morphologyEx(imgCanny, cv2.MORPH_TOPHAT, kernel) # Tophat

################## Show images ########################

images = [img, imgBlur, imgCanny, imgDilation, imgErosion, imgOpening, imgClosing, imgGradient, imgTophat]
titles = ['Original', 'Blur', 'Canny', 'Dilate', 'Erode', 'Open', 'Close', 'Gradient', 'Tophat']

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


