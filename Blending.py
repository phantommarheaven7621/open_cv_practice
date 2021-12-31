import cv2
import numpy as np

img = cv2.imread('morning_evening.jpg')
morning = img[:, :742, :]
evening = img[:, 742:, :]

morning = cv2.resize(morning, (512, 512))
evening = cv2.resize(evening, (512, 512))

# Gaussian pyramids for morning
morning_copy = morning.copy()
gaussian_morning = [morning_copy]

for i in range(6):
    morning_copy = cv2.pyrDown(morning_copy)
    gaussian_morning.append(morning_copy)

# Gaussian pyramids for evening
evening_copy = evening.copy()
gaussian_evening = [evening_copy]

for i in range(6):
    evening_copy = cv2.pyrDown(evening_copy)
    gaussian_evening.append(evening_copy)

# Laplacian pyramids for morning
morning_copy = gaussian_morning[-1]
pyrUp_morning = [morning_copy]
laplacian_morning = []

for i in range(len(gaussian_morning)-1, 0, -1):
    morning_copy = cv2.pyrUp(gaussian_morning[i])
    pyrUp_morning.append(morning_copy)

pyrUp_morning.reverse()

for a, b in zip(gaussian_morning, pyrUp_morning):
     laplacian_morning.append(cv2.subtract(a, b))

# Laplacian pyramids for evening
evening_copy = gaussian_evening[-1]
pyrUp_evening = [evening_copy]
laplacian_evening = []

for i in range(len(gaussian_evening)-1, 0, -1):
    evening_copy = cv2.pyrUp(gaussian_evening[i])
    pyrUp_evening.append(evening_copy)

pyrUp_evening.reverse()

for a, b in zip(gaussian_evening, pyrUp_evening):
     laplacian_evening.append(cv2.subtract(a, b))

# Combine 2 images
morning_evening_pyramid = []

for mor, eve in zip(laplacian_morning, laplacian_evening):
    add_img = np.hstack((mor, eve))
    morning_evening_pyramid.append(add_img)

morning_evening_pyramid.reverse()

# Reconstruct images
morning_evening_reconstruct = morning_evening_pyramid[0]

for i in range(len(morning_evening_pyramid)-1):
    morning_evening_reconstruct = cv2.pyrUp(morning_evening_reconstruct)
    morning_evening_reconstruct = cv2.add(morning_evening_pyramid[i+1], morning_evening_reconstruct)

# for i in range(len(morning_evening_pyramid)):
#     cv2.imshow(str(i), morning_evening_pyramid[i])

cv2.imshow('Original Image', img)
cv2.imshow('Morning', morning)
cv2.imshow('Evening', evening)
cv2.imshow('Blending', morning_evening_reconstruct)
cv2.waitKey(0)
cv2.destroyAllWindows()