import cv2 as cv
import numpy as np

# Read image
img = cv.imread('Resources/Photos/park.jpg')
cv.imshow('Park', img)

# Averaging - (3,3) is the kernel size. Larger kernel size usually results in stronger blurs
average = cv.blur(img, (3, 3))
cv.imshow('Average Blur', average)

# Gaussian Blur
gauss = cv.GaussianBlur(img, (3, 3), 0)
cv.imshow("Gaussian Blur", gauss)

# Median Blur
median = cv.medianBlur(img, 3)
cv.imshow("Median Blur", median)

# Bilateral Blur
bilateral = cv.bilateralFilter(img, 10, 15, 15)
cv.imshow("Bilateral", bilateral)

cv.waitKey(0)
