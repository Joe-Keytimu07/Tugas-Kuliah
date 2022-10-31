

import cv2 
# load an image 
# image = cv2.imread("daun.png")
# load an image in grayscale
image = cv2.imread("SketsaPensil.jpg",0)
# # display grayscale image 
# cv2.imshow("daun",image_gray)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
print (image.shape)
print (image.ndim)



# import cv2
# import numpy as np
# # from skimage.util 
# import random_noise
# from matplotlib import pyplot as plt

# # Load citra yang akan digunakan
# img = cv2.imread("daun.png")
# ori_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# # Menambahkan speckle noise ke citra original.
# noise_img = random_noise(ori_img, mode='speckle', mean=0.3, var=0.5)

# # Fungsi diatas menghasilkan citra dengan nilai float
# # yang berada pada rentang nilai [0,1], sehingga
# # perlu diubah menjadi format uint8 dengan rentang
# # nilai [0,255]
# noise_img = np.array(255 * noise_img, dtype='uint8')

# # Menampilkan citra dengan noise
# plt.subplot(121), plt.imshow(ori_img), plt.title('Original Image')
# plt.xticks([]), plt.yticks([])
# plt.subplot(122), plt.imshow(noise_img), plt.title('Speckle Noise Image')
# plt.show()