import cv2
import matplotlib.pyplot as plt
import numpy as np
import Util

img = cv2.imread("1.jpg")
cv2.namedWindow("1.jpg", cv2.WINDOW_NORMAL)
cv2.imshow("1.jpg", img)
histb = cv2.calcHist([img], [0], None, [256], [0, 255])
histg = cv2.calcHist([img], [1], None, [256], [0, 255])
histr = cv2.calcHist([img], [2], None, [256], [0, 255])

plt.plot(histb, color="b")
plt.plot(histg, color="g")
plt.plot(histr, color="r")
plt.show()

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

low_hsv = np.array([0, 43, 46])
high_hsv = np.array([20, 255, 255])

mask = cv2.inRange(hsv, lowerb=low_hsv, upperb=high_hsv)
cv2.namedWindow("mask", cv2.WINDOW_NORMAL)
cv2.imshow("mask", mask)
cv2.waitKey()

region = Util.detect(mask)
cv2.drawContours(img, region, cv2.FILLED, (0, 0, 0), -1)
cv2.namedWindow("img", cv2.WINDOW_NORMAL)
cv2.imshow("img", img)
cv2.waitKey()
cv2.destroyAllWindows()
