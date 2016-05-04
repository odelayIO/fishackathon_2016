import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read the image, convert it into grayscale, and make in binary image for threshold value of 1.

img1 = cv2.imread('1.jpg')
gray1 = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
img2 = cv2.imread('2.jpg')
gray2 = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)

cv2.imshow('Billfish',gray1)
cv2.imshow('Bluefin Tuna',gray2)
cv2.waitKey(0)

# Use first image
n = gray1.shape
a = []
for i in range(0,n[1]):
  a.append(255-np.mean(gray1[:,i]))




# Use first image
n = gray2.shape
b = []
for i in range(0,n[1]):
  b.append(255-np.mean(gray2[:,i]))

plt.figure(1)
t = range(0,n[1]);
plt.plot(t,a,'b',t,b,'r')
plt.show()


#cv2.imshow('Billfish',gray1)
#cv2.waitKey(0)
