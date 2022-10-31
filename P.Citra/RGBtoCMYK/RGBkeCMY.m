function [C,M,Y,K] = RGBkeCMY(R,G,B)
if max(max(R)) > 1.0 || max(max(G)) >1.0 || max(max(B))>1.0
  R = double(R) / 255;
  G = double(G) / 255;
  B = double(B) / 255;
end
u=0.5;
b=1;
[tinggi, lebar] = size (R);
for m=1: tinggi
  for n=1:lebar
    kp = min([(1-R(m,n)) (1-G(m,n)) (1-B(m,n))]);
    if kp == 1
        C(m,n)=0;
        M(m,n)=0;
        Y(m,n)=0;
     else
        C(m,n) = (1.0 -R(m,n) - u * kp);
        M(m,n) = (1.0 -G(m,n) - u * kp);
        Y(m,n) = (1.0 -B(m,n) - u * kp);
        K(m,n) = b * kp;
    endif
  endfor
endfor
%konversi ke jangkauan [0,255]
C = uint8(C*255);
M = uint8(M*255);
Y = uint8(Y*255);
K = uint8(K*255);
endfunction 
%cara penggunaan pada satu pixel :
%>>[C,M,Y,K] = RGBkeCMY(171,215,170)
%C = 64
%M = 20
%y = 65
%K = 40

%contoh konversi untuk seluruh citra sebagai berikut :
%>> img = imread('');
%>> RGBkeCMY(img(:,:,1),img(:,:,2),img(:,:,3));



      
      


