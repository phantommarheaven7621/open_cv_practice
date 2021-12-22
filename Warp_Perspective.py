import numpy as np
import cv2

cap = cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

width, height = 300, 300

while True:
    _, frame = cap.read()

    grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(grey, 1.3, 5)

    for x,y,w,h in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (255, 0, 0), 3)

        point1 = np.float32([[x, y], [x + w, y], [x, y + h], [x + w, y + h]])
        point2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
        matrix = cv2.getPerspectiveTransform(point1, point2)
        output = cv2.warpPerspective(frame, matrix, (width, height))
        cv2.imshow('output', output)


    cv2.imshow('frame', frame)

    if cv2.waitKey(1) ==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
