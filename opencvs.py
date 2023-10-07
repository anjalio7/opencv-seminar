# importing the library
import cv2
import sys

# reading the images
# img = cv2.imread('C:\Users\HP\Downloads\Background-Remover-Flask-App-using-Python-main\Background-Remover-Flask-App-using-Python-main\logo.jpg')

img = cv2.imread('logo.jpg')

if img is None:
    sys.exit('Image not found')

cv2.imshow('Logo Image', img)

# dimensions of image
print('shape of image is ', img.shape)

# resize images
img1 = cv2.resize(img, ((675 // 2), (1200 // 2)))
# cv2.imshow('Resized image ', img1)

# cropping the images
img2 = img[100:500, 100:500]
# cv2.imshow('Cropped Image ', img2)

# blur the images
img3 = cv2.blur(img, (9, 9))
# cv2.imshow('Blur Image', img3)

# flip the image
img4 = cv2.flip(img, 0)
# flipcode - 0 for horizontal, 1 for vertical, -1 for both axis
cv2.imshow('Horizontal flipped image', img4)



w = cv2.waitKey(0)
if w == ord('s'):
    cv2.imwrite('flipped.jpg', img4)