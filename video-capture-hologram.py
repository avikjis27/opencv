import numpy as np
import cv2


img = cv2.imread('.\hologram.jpg',cv2.WINDOW_NORMAL)
cap = cv2.VideoCapture(0)
width = (int)(cap.get(3)/4)
height = (int)(cap.get(4))

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #frame[0:height,0:width, 0:3] = randomGrayImage
    gray[height-140:height-12,width-140:width-12 ] = img

    # Display the resulting frame
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
