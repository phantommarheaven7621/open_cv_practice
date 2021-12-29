import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('bill.jpg', -1)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
grey = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

################# Thresholding #################

_, th1 = cv2.threshold(grey, 100, 255, cv2.THRESH_BINARY) # <100 --> 0, >=100 --> 255
_, th2 = cv2.threshold(grey, 100, 255, cv2.THRESH_BINARY_INV) # >=100 --> 255, <100 --> 0
_, th3 = cv2.threshold(grey, 100, 255, cv2.THRESH_TRUNC) # all pixels greater than 100 set to 255
_, th4 = cv2.threshold(grey, 100, 255, cv2.THRESH_TOZERO) # all pixels smaller than 100 set to 0
_, th5 = cv2.threshold(grey, 100, 255, cv2.THRESH_TOZERO_INV) # all pixels greater than 100 set to 0

################# Adaptive Thresholding #################

ada_th1 = cv2.adaptiveThreshold(grey, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
ada_th2 = cv2.adaptiveThreshold(grey, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

images = [img, grey, th1, th2, th3, th4, th5, ada_th1, ada_th2]
titles = ['original', 'grey', 'thresh binary', 'thresh binary inverse',
          'thresh trunc', 'thresh to zero', 'thresh to zero inverse',
          'Adaptive thresh mean C', 'Adaptive thresh gaussian C']

################# Show images with matplotlib #################

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
