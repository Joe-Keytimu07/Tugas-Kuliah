# menggunakan library pillow 
from PIL import Image
# fungsi citra biner
def citra_biner(nilai_ambang):
    # konversi gambar RGB ke grayscale
    CITRA_GRAYSCALE = Image.open('burung.jpg').convert('L')
    # untuk akses pixel dari citra grayscale
    PIXEL_GRAYSCALE = CITRA_GRAYSCALE.load()

    # untuk batas mengetahui ukuran gambar yang akan di olah.
    # menggunakan var size
    ukuran_vertikal = CITRA_GRAYSCALE.size[1]
    ukuran_horizontal = CITRA_GRAYSCALE.size[0]
    

    for y in range(ukuran_vertikal):
        for x in range(ukuran_horizontal):
            # kondisi jika nilai pixel < nilai ambang maka matrixnya =0
            if PIXEL_GRAYSCALE[x, y] < nilai_ambang:
                PIXEL_GRAYSCALE[x, y] = 0
            # kondisi jika nilai pixel > nilai ambang maka matrixnya =1
            else:
                PIXEL_GRAYSCALE[x, y] = 255
    
    # untuk menyimpan hasil pengolahan citra 
    save_gambar = 'gambar_biner_' + str(nilai_ambang) + '.jpg'
    CITRA_GRAYSCALE.save( save_gambar)


citra_biner(108)