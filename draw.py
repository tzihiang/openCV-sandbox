import cv2 as cv
import numpy as np

# Create a blank "image"

blank = np.zeros((500, 500, 3), dtype='uint8')
cv.imshow('Blank', blank)

# Paint the image a certain color
# blank[:] = 0, 255, 0  # Populate each pixel to be green

# Draw a rectangle
# cv.rectangle(blank, (0, 0), (250, 250), (255, 255, 255), thickness=2)
# Another way to draw: Call the size array of the original image
cv.rectangle(blank, (0, 0), (blank.shape[1]//2,
                             blank.shape[0]//2), (0, 255, 0), thickness=-1)
cv.imshow('Rectancgle', blank)

# Draw a circle
cv.circle(blank, (blank.shape[1]//2,
                  blank.shape[1]//2), 40, (0, 0, 255), thickness=-1)
cv.imshow('Circle', blank)

# Draw a line
cv.line(blank, (100, 100), (300, 400), (255, 255, 255), thickness=3)
cv.imshow('line', blank)

# Add text
cv.putText(blank, "Hello world", (225, 225),
           cv.FONT_HERSHEY_TRIPLEX, 1.0, (0, 255, 0), 2)
cv.imshow('Text', blank)

cv.waitKey(0)
