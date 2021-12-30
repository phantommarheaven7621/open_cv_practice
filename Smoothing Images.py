import cv2
import numpy as np
import matplotlib.pyplot as plt

################## Prepare Images ######################

img = cv2.imread('doreamon.jpg', -1)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img = img[195:605, 286:607]

################## Smoothing Images ######################

kernel = np.ones((5, 5), np.uint8) / (5*5)

homogeneous_blur = cv2.filter2D(img, -1, kernel)
blur = cv2.blur(img, (5, 5)) # The same as homogeneous blurring
gaussian_blur = cv2.GaussianBlur(img, (5, 5), 0)
median_blur = cv2.medianBlur(img, 5) # It's better for pepper and salt images
bilateralFilter = cv2.bilateralFilter(img, 9, 75, 75) # Preserve the edges

################## Show images ########################

images = [img, homogeneous_blur, blur, gaussian_blur, median_blur, bilateralFilter]
titles = ['Original', 'Homogeneous Blur', 'Blur', 'Gaussian Blur', 'Median Blur', 'Bilateral Filter']

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


