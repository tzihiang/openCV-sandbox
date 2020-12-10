import cv2 as cv
import numpy as np

# Read image
img = cv.imread('Resources/Photos/park.jpg')
cv.imshow('Park', img)

# Translation


def translate(img, x, y):
    transMat = np.float32([[1, 0, x], [0, 1, y]])      # Translation matrix
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

# Left-Right: x-axis, Top-Bottom: y-axis (Note that for y, top is -ve, bottom is +ve)


translated = translate(img, 100, 100)
cv.imshow('Translated', translated)

# Rotation


def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2, height//2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)
    return cv.warpAffine(img, rotMat, dimensions)


rotated = rotate(img, 45)
cv.imshow('Rotate', rotated)

# Resizing
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_LINEAR)
cv.imshow('Resize', resized)

# Flip an image
# 0 if flipping vertically, 1 for horizontally, -1 for both
flip = cv.flip(img, -1)
cv.imshow('Flip', flip)

# Cropping
cropped = img[200:400, 200:400]
cv.imshow("Cropped", cropped)

cv.waitKey(0)
