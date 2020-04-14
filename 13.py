import cv2 as cv
from func import *

SIZE = (400, 300)

RECT = np.float32([[0, 299],
                   [399, 299],
                   [399, 0],
                   [0, 0]])

TRAP = np.float32([[0, 299],
                   [399, 299],
                   [320, 200],
                   [80, 200]])

image = cv.VideoCapture(1)
while(cv.waitKey(1) != 32):
    a, cap = image.read()
    cv.imshow("im", cap)
    cv.imshow("binary", trans_perspective(binarize(cap), TRAP, RECT, SIZE))

cv.destroyAllWindows()
