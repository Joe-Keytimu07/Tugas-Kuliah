
import cv2 
import numpy as np
import statistics as s

img = cv2.imread('burung.jpg',0)
# pix_val = list(img.getdata())


contoh_data = np.array(
        [
            [165, 250, 55, 145, 145], 
            [178, 68, 60, 25,67], 
            [60, 80, 62, 180, 186], 
            [55, 145, 60, 66, 69], 
            [68, 60, 55, 50, 145]
            ]
        )

def citra_biner(input,T):
    kiri = []
    kanan = []
    for y in range(len(input)):
        for x in range(len(input[0])):
            if input[y,x] < T:
                kiri.append(input[y,x]) ;
            else:
                kanan.append(input[y,x])
    return kanan,kiri
     

def ambang(input,T):
    t1 = T
    t2 = 0
    while t1 != t2:
        t2 = t1
        kiri,kanan = citra_biner(input,t2)
        x1 = s.mean(kiri)
        x2 = s.mean(kanan)
        t1 = round((x1 + x2)/2)
    return t2

t = ambang(img,106)
print(t)