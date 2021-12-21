import numpy as np
import cv2

cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

while True:
    _, frame = cap.read()

    grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(grey, 1.3, 5)
    eyes = eye_cascade.detectMultiScale(grey, 1.3, 5)
    for x, y, w, h in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 3)

    for e_x, e_y, e_w, e_h in eyes:
        cv2.rectangle(frame, (e_x, e_y), (e_x + e_w, e_y + e_h), (0, 255, 0), 3)




    cv2.imshow('frame', frame)
    cv2.imshow('grey', grey)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()