import numpy as np
import cv2

# Load an color image in grayscale
img = cv2.imread('.\girl.png',cv2.WINDOW_NORMAL)
cv2.imshow('kirigami',img)
key = cv2.waitKey(0)
if key == 27:
    cv2.destroyAllWindows()
elif key == ord('s'):
    cv2.imwrite('.\\temp\girl_1.png',img)
    cv2.destroyAllWindows()
