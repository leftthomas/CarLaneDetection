import cv2
import matplotlib.image as mplimg

img = mplimg.imread('../resources/lane.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
cv2.imshow('gr', gray)
# 程序暂停
cv2.waitKey(0)
# Note that if you use cv2.imread() to read image, the image will
# be in format BGR.
