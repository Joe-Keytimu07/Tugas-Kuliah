% Algoritma median

Gambar = imread('D:\Tugas Kuliah\Tugas-Kuliah\P.Citra\Praktikum4\gambar.jpeg');
[Tinggi, Lebar] = size(Gambar);

for baris=2 : Tinggi-1
  for kolom=2 : Lebar-1
    Data = [Gambar(baris-1, kolom-1) ...
            Gambar(baris-1, kolom) ...
            Gambar(baris-1, kolom+1) ...
            Gambar(baris, kolom-1) ...
            Gambar(baris, kolom) ...
            Gambar(baris, kolom+1) ...
            Gambar(baris+1, kolom-1) ...
            Gambar(baris+1, kolom) ...
            Gambar(baris+1, kolom+1)];

     % Mengurutkan data
     for i = 1:8
       for j = i+1:9
         if Data(i) > Data(j)
           Tampung = Data(i);
           Data(i) = Data(j);
           Data(j) = Tampung;
         endif
       endfor
     endfor

     % Mengambl nilai media
     G(baris, kolom) = Data(5);
  endfor
endfor

subplot(1,2,1), imshow(Gambar);
subplot(1,2,2), imshow(G);


