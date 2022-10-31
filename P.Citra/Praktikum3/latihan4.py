# import turtle

# pen = turtle.Turtle()

# def curve():
#     for i in range(200):
#         pen.right(1)
#         pen.forward(1)

# def heart():
#     pen.fillcolor('red')
#     pen.begin_fill()
#     pen.left(140)
#     pen.forward(113)
#     curve()
#     pen.left(120)
#     curve()
#     pen.forward(112)
#     pen.end_fill()

# def txt():
#     pen.up()
#     pen.setpos(-68, 95)
#     pen.down()
#     pen.color('lightgreen')
#     pen.write('I Love You', font=("Verdana", 12, "bold"))

# heart()
# txt()
# pen.ht()

# mengubah gambar menjadi sketsa pensil 
# import cv2

# myimage = cv2.imread("daun.png")
# grayImage = cv2.cvtColor(myimage, cv2.COLOR_RGB2GRAY)
# # grayImageInv = 255 - grayImage
# grayImageInv = cv2.GaussianBlur(grayImageInv, (21,21), 0)
# output = cv2.divide(grayImage, 255-grayImageInv, scale=256.0)
# filename = 'SketsaPensil.jpg'
# cv2.imwrite(filename, output)
# cv2.namedWindow("Gambar Asli", cv2.WINDOW_AUTOSIZE)
# cv2.imshow("Gambar Asli", myimage)
# cv2.imshow("Gambar Sketsa Pensil", output)
# cv2.waitKey()

import cv2
import numpy as np

myimage = cv2.imread("daun.png")
grayImage = cv2.cvtColor(myimage, cv2.COLOR_RGB2GRAY)

grayImageInv = cv2.cvtColor(grayImage, cv2.COLOR_GRAY2BGR)
image_show = np.hstack((myimage,grayImageInv))
cv2.imshow("Gambar Asli", image_show)
cv2.waitKey()