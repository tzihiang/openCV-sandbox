import cv2 as cv
import numpy as np

# Read image
img = cv.imread('Resources/Photos/park.jpg')
cv.imshow('Park', img)

# Show the image in their respective colors in the color channel
blank = np.zeros(img.shape[:2], dtype='uint8')

b, g, r = cv.split(img)

# Order is important as each b,g and r represents the given colour values of each pixel after cv.split()
# What is being done here is passing back the values to a blank canvas to display 1 color channel only
blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])

cv.imshow('Blue', b)
cv.imshow('Blued', blue)

cv.imshow('Greened', green)

# cv.imshow('Green', g)
# cv.imshow('Red', r)


print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

# Merge the color channels
merge = cv.merge([b, g, r])

cv.waitKey(0)
