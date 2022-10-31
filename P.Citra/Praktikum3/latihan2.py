# import cv2 as gambar
# img = gambar.imread ('daun.png')

# print(img.shape)
# print(img[0][0][0])
# print(img[0][0][10])
# print(img[0][0][20])
# print(gambar.mean(img))

# from PIL import Image

# CITRA = Image.open("daun.png")
# PIXEL = CITRA.load()

# # cara mengakses aras titik
# x = 3
# y = 8
# print(PIXEL[x, y])   # nilai RGB dari pixel (x, y)
# print(PIXEL[x, y][0])  # nilai R dari pixel (x, y)
# print(PIXEL[x, y][1])  # nilai G dari pixel (x, y)
# print(PIXEL[x, y][2])  # nilai B dari pixel (x, y)


# Dalam transformasi affine, semua garis sejajar dalam gambar asli akan tetap sejajar dalam gambar output
import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('daun.png')
rows,cols,ch = img.shape
 
pts1 = np.float32([[50,50],[200,50],[50,200]])
pts2 = np.float32([[10,100],[200,50],[100,250]])
# cv2.getAffineTransform akan membuat matriks 2×3 yang akan diteruskan ke cv2.warpAffine.
M = cv2.getAffineTransform(pts1,pts2)
 
dst = cv2.warpAffine(img,M,(cols,rows))
 
plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.show()