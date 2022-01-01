import cv2
import numpy as np

img = cv2.imread('shape1.png')
img = img[50:360, 25:575]
grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#blur = cv2.GaussianBlur(grey, (1, 1), 0.5)
# bilateralFilter = cv2.bilateralFilter(grey, 15, 75, 75)
_, thresh = cv2.threshold(grey, 240, 250, cv2.THRESH_BINARY)
canny = cv2.Canny(thresh, 200, 200)


contours, hierarchy = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

for contour in contours:
    approx = cv2.approxPolyDP(contour, 0.01*cv2.arcLength(contour, True), True)
    print(contour.shape)
    print(approx.shape)
    for a in approx:
        cv2.circle(img, tuple(a.ravel()), 3, (0, 0, 255), 3)
    cv2.drawContours(img, [contour], 0, (0, 0, 0), 5)

    (x, y, w, h) = cv2.boundingRect(contour)

    if len(approx) == 3:
        cv2.putText(img, 'Triangle', (x, y+h+20), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
    elif len(approx) == 4:
        ratio = float(w)/h
        if (ratio >=0.9) and (ratio <=1.1):
            cv2.putText(img, 'Square', (x, y + h + 20), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
        else:
            cv2.putText(img, 'Rectangle', (x, y + h + 20), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
    elif len(approx) == 10:
        cv2.putText(img, 'Star', (x, y + h + 20), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
    else:
        cv2.putText(img, 'Irregular', (x, y + h + 20), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
# corners = cv2.goodFeaturesToTrack(canny, 1000, 0.01, 15)
# corners = corners.astype(int)
#
# for corner in corners:
#     x, y = corner.ravel()
#     cv2.circle(img_copy, (x, y), 1, (0, 150, 255), 3)

'''
count = 1
for index, contour in enumerate(contours):
    # Find area of contour:
    area = cv2.contourArea(contour)
    if area > 500:
        print('Shape {}: {}'.format(count, contour.shape))
        print('Area = ', area)

        # Find perimeter of contour:
        perimeter = cv2.arcLength(contour, True)
        print('Perimeter', perimeter)

        # Find
        approx = cv2.approxPolyDP(contour, 0.09*perimeter, True)
        print(len(approx))

        # Draw contour on an image
        cv2.drawContours(img_copy, contour, -1, (200, 200, 20), 4)
        count += 1
        print('----------------')
'''

cv2.imshow('shape image', img)
# cv2.imshow('grey image', grey)
# cv2.imshow('blur image', blur)
# cv2.imshow('canny', canny)
if cv2.waitKey(0) != ord('q'):
    pass
cv2.destroyAllWindows()