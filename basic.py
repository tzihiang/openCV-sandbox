import cv2 as cv

# Read image
img = cv.imread('Resources/Photos/cat.jpg')
cv.imshow('Cat', img)

# Convert to greyscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Blur
blur = cv.GaussianBlur(img, (3, 3), cv.BORDER_DEFAULT)
cv.imshow("Blur", blur)

# Edge cascade: To find edges
# You can apply this to a blurred image to get sharper edges
canny = cv.Canny(img, 125, 175)
cv.imshow("Canny Edges", canny)

# Dilating an image
dilated = cv.dilate(canny, (7, 7), iterations=3)
cv.imshow('Dilated', dilated)

# Eroding
eroded = cv.erode(dilated, (3, 3), iterations=1)
cv.imshow('Eroded', eroded)

# Resize
resize = cv.resize(img, (500, 500))
cv.imshow('Resized', resize)

# Crop
cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)
