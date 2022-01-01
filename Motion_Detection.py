import cv2
import numpy as np

cap = cv2.VideoCapture('WalkingPeople.mp4')
ret, frame1 = cap.read()
ret, frame2 = cap.read()

while (cap.isOpened()):
    diff = cv2.absdiff(frame1, frame2)
    grey = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    _, binary = cv2.threshold(grey, 20, 255, cv2.THRESH_BINARY)
    kernel = np.ones((7, 7), np.uint8)
    dilate = cv2.dilate(binary, kernel=kernel, iterations=1)

    contours, _ = cv2.findContours(dilate, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # cv2.drawContours(frame1, contours, -1, (200, 200, 0), 2)

    for contour in contours:
        (x, y, w, h) = cv2.boundingRect(contour)

        if cv2.contourArea(contour) < 1900:
            continue
        else:
            cv2.rectangle(frame1, (x,y), (x+w, y+h), (0, 200, 0), 2)

    # cv2.imshow('diff', diff)
    # cv2.imshow('grey', grey)
    # cv2.imshow('binary', binary)
    # cv2.imshow('dilate', dilate)
    cv2.imshow('contours', frame1)

    frame1 = frame2.copy()
    ret, frame2 = cap.read()

    if cv2.waitKey(8) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()