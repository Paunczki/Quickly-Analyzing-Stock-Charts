import cv2
import numpy as np
# Read pictures
img=cv2.imread('newImages/image1.png')
# Image zoom
#img = cv2.resize(img,None,fx=0.5,fy=0.5)
#rows,cols,channels = img.shape
#print(rows,cols,channels)
cv2.imshow('img',img)

# Picture to grayscale
img_grayscale = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

thresh, img_black = cv2.threshold(img_grayscale, 100, 255, cv2.THRESH_BINARY)

#input_image.save("newImages/image_1.png", format="png")

cv2.imshow('newImages/image1.png', img_black)  

cv2.waitKey(0)

cv2.destroyAllWindows()