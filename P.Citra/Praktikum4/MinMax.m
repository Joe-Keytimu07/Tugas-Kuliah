% Algoritma Minumum-Maksimum

Gambar = imread('D:\Tugas Kuliah\Tugas-Kuliah\P.Citra\Praktikum4\gambar.jpeg');
Ukuran = size(Gambar);
Tinggi = Ukuran(1);
Lebar = Ukuran(2);

Data = Gambar;

for baris=2 : Tinggi-1
  for kolom=2 : Lebar-1
    MinPiksel = min([Gambar(baris-1, kolom-1) ...
                Gambar(baris-1, kolom) Gambar(baris, kolom+1) ...
                Gambar(baris, kolom-1) ...
                Gambar(baris, kolom+1) Gambar(baris+1, kolom-1) ...
                Gambar(baris+1, kolom) Gambar(baris+1, kolom+1)]);
    MaksPiksel = min([Gambar(baris-1, kolom-1) ...
                Gambar(baris-1, kolom) Gambar(baris, kolom+1) ...
                Gambar(baris, kolom-1) ...
                Gambar(baris, kolom+1) Gambar(baris+1, kolom-1) ...
                Gambar(baris+1, kolom) Gambar(baris+1, kolom+1)]);
    if Gambar(baris, kolom) < MinPiksel
       Data(baris, kolom) = MinPiksel;
    else
       if Gambar(baris, kolom) > MaksPiksel
          Data(baris, kolom) = MaksPiksel;
       else
          Data(baris, kolom) = Gambar(baris, kolom);
       endif
    endif
  endfor
endfor

subplot(1,2,1), imshow(Gambar);
subplot(1,2,2), imshow(Data);


