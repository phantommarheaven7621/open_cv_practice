import cv2

img = cv2.imread('doreamon.jpg')
img_copy = img.copy()

def click_event(event, x, y, flags, param):
    global img_copy
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img_copy, (x, y), 3, (0, 0, 0), -1)
        string = '(' + str(x) + ', ' + str(y) + ')'
        font = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
        cv2.putText(img_copy, string, (x, y), font, 1, (0, 0, 0), 2)
        cv2.imshow('image', img_copy)

    elif event == cv2.EVENT_RBUTTONDOWN:
        img_copy = img.copy()
        cv2.imshow('image', img_copy)


cv2.imshow('image', img_copy)
cv2.setMouseCallback('image', click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()