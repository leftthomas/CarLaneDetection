import cv2
import matplotlib.image as mplimg

img = mplimg.imread('../resources/lane.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
# cv2.imshow('gray', gray)
# 程序暂停
# cv2.waitKey(0)
# Note that if you use cv2.imread() to read image, the image will
# be in format BGR.

blur_ksize = 5  # Gaussian blur kernel size
blur_gray = cv2.GaussianBlur(gray, (blur_ksize, blur_ksize), 0, 0)

canny_lthreshold = 50  # Canny edge detection low threshold
canny_hthreshold = 150  # Canny edge detection high threshold
edges = cv2.Canny(blur_gray, canny_lthreshold, canny_hthreshold)
cv2.imshow('edges', edges)
cv2.waitKey(0)
