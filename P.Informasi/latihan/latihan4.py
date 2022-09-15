
# thn_masuk = 2019
# x= 2019
# if x == thn_masuk:
#     print("selamat datang mahasiswa baru")
# else :
#     y=x-thn_masuk
#     print("selamat datang anda telah melewati tahun ke -{y}")
#     if y==1:
#         print("anda telah mengambil matkul algoritma dan pemrograman")
#     elif y==2 :
#         print ("anda telah mengambil matkul pemrograman berorientasi objek")
#     elif y==3:
#         print ("anda telah memilih bidang minat dari 3 bidang minat")
#     else :
#          print ("anda sedang mengambil metopen atau skripsi")
# def fibonnaci (x):
#   if x <=1:
#     return 0
#   elif x == 2:
#     return 1
#   else:
#     x1 = fibonnaci (x-1)
#     x2 = fibonnaci (x-2)
#     return x1+x2

# x= (input ("masukan angka :"))
# print(fibonnaci(x))

#latihan 8
def fibonnaci(x):
  if x<0:
    return 0
  elif x==2 or x==1:
    return 1
  elif x>2:
    x1=fibonnaci (x-1)
    x2=fibonnaci (x-2)
    x1+x2
    return x1+x2

x=int(input("masukan angka :"))
i=0
while i<x-1:
  i+=1
  j=0
  txt=""
  while j<i:
    j+1
    txt+=str(fibonnaci(j))
  print (txt)