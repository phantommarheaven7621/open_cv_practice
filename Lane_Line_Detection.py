import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('laneline1.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
grey = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
canny = cv2.Canny(grey, 100, 150)

height = img.shape[0]
width = img.shape[1]

ROI = np.array([
    [0, height],
    [width/2, height/2],
    [width, height]
])

def mask_img(img, ROI):
    mask = np.zeros_like(img)
    cv2.fillPoly(mask, pts=np.int32([ROI]), color=255),
    masked_img = cv2.bitwise_and(mask, img)
    return masked_img

def draw_lines(img, lines):
    for line in lines:
        [[x1, y1, x2, y2]] = line
        cv2.line(img, (x1, y1), (x2, y2), (255, 255, 0), 2)

masked_img = mask_img(canny, ROI)

lines = cv2.HoughLinesP(
    masked_img,
    rho=6,
    theta=np.pi/60,
    threshold=70,
    lines=np.array([]),
    minLineLength=10,
    maxLineGap=10
)

draw_lines(img, lines)

################## Show images ########################

images = [img, masked_img]
titles = ['Original', 'masked_img']

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