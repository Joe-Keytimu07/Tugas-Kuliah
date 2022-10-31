# code program berikut di gunakan untuk memanggil atau membuka dambar dengan menggunakan format tertentu.
# pada program berikut menggunakan library open cv dengan bahasa pemrograman python 
# install library open cv
import cv2
# penambahan gambar sesuai dengan nama/ format gambar 
image= cv2.imread("daun.png",cv2.IMREAD_COLOR)
# menampilkan gambar 
cv2.imshow ("daun",image)

# menyimpan gambar 
# cv2.imwrite('save_daun.png')

# menunda windows terdestroy
cv2.waitKey(0) 
# mendestroy windows 
cv2.destroyALLWindow()