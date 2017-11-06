import numpy as np
import cv2
import os

cap = cv2.VideoCapture(0)
width = (int)(cap.get(3)/4)
height = (int)(cap.get(4))

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    randomByteArray = bytearray(os.urandom(width * height * 3))
    flatNumpyArray = np.array(randomByteArray)
    randomGrayImage = flatNumpyArray.reshape(height, width, 3)
    # Our operations on the frame come here
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    frame[0:height,0:width, 0:3] = randomGrayImage


    # Display the resulting frame
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
