import numpy as np
import cv2

# Load an color image in grayscale
img = cv2.imread('img1.jpg',1)
#cv2.imwrite('messigray.png',img)
#face = img[220:300, 310:360]
#img[100:180, 100:150] = face
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()