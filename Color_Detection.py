import cv2
import numpy as np

cap = cv2.VideoCapture(0)
width = int(cap.get(3))
height = int(cap.get(4))
print('height:', height)
print('width:', width)
print('height:', cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print('width:', cap.get(cv2.CAP_PROP_FRAME_WIDTH))

def nothing(x):
    pass

cv2.namedWindow('Trackbars')

cv2.createTrackbar('L - H', 'Trackbars', 0, 179, nothing)
cv2.createTrackbar('H - H', 'Trackbars', 0, 179, nothing)
cv2.createTrackbar('L - S', 'Trackbars', 0, 255, nothing)
cv2.createTrackbar('H - S', 'Trackbars', 0, 255, nothing)
cv2.createTrackbar('L - V', 'Trackbars', 0, 255, nothing)
cv2.createTrackbar('H - V', 'Trackbars', 0, 255, nothing)


while True:
    ret, frame = cap.read()

    l_h = cv2.getTrackbarPos('L - H', 'Trackbars')
    h_h = cv2.getTrackbarPos('H - H', 'Trackbars')
    l_s = cv2.getTrackbarPos('L - S', 'Trackbars')
    h_s = cv2.getTrackbarPos('H - S', 'Trackbars')
    l_v = cv2.getTrackbarPos('L - V', 'Trackbars')
    h_v = cv2.getTrackbarPos('H - V', 'Trackbars')

    hsv = cv2.cvtColor(frame, cv2.COLOR_RGB2HSV)
    lower_red = np.array([l_h, l_s, l_v])
    upper_red = np.array([h_h, h_s, h_v])

    mask = cv2.inRange(frame, lower_red, upper_red)
    result = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow('hsv', hsv)
    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('result', result)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()





