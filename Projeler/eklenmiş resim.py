import cv2
import numpy as np

resim=cv2.imread("projeler/tree.png")      # Kesiti alınacak resmi okuma
yol=cv2.imread("projeler/yol bulma.png")    #kesit eklenecek resim okuma

kesit=resim[50:250,200:350]   #birinci resimden bir bölge seçme

yol[100:300,150:300]=kesit     #seçilen bölgeyi ikinci resme ekleme

cv2.imshow("Birleşmiş iki resim",yol)  #birleştirdiğimiz iki resmi yazdırma

cv2.waitKey(0)
cv2.destroyAllWindows()