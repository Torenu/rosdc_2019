import cv2 as cv
from func import *

image = cv.imread("home_pi_imaaage.jpg")
cv.imshow("im", image)

binarize(image, d=True)

cv.waitKey(0)