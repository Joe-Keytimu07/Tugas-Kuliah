from contextlib import closing
from email import iterators
from errno import EPROTONOSUPPORT
# import cv2 as cv
# img = cv.imread('citra.jpg')

# cv.imshow('original',img)


# erosi= cv.erode(img,Kernel,iterations =1)
# dilasi= cv.dilate(erosi,Kernel,iterations =1)
# opening = cv.morphologyEx(dilasi,cv.MORPH_OPEN,Kernel)
# closing = cv,morphologyEx(opening,cv.MORPH_CLOSE,Kernel)

# cv.imshow('erosi', erosi)
# cv.imshow('dilasi', dilasi)

# cv.waitKey(0)
# cv.destroyALLWindows()

	
import cv2
import numpy as np
from matplotlib import pyplot as plt
 
img = cv2.imread('citra.jpg')
 
kernel = np.ones((3,3),np.uint8)
dilation = cv2.dilate(img,kernel,iterations = 1)
 
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(dilation),plt.title('dilation')
plt.xticks([]), plt.yticks([])
plt.show()

