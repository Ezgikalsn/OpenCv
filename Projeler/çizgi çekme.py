from gettext import npgettext
import cv2
import numpy as np

agacresmi= cv2.imread("projeler/tree.png")       #resmi okuma

print("boyut: "+str(agacresmi.shape))      #resmin boyutlarını öğrenme

agacresmi[50,30]=[0,0,0]      #resimde (50,30) denk gelen matrisin siyaha boyanması

for i in range(500):     #resimde for döngüsüyle belirlenen matrisleri siyaha boyayarak çizgi elde etme
    agacresmi[70,i]=[0,0,0]

cv2.imshow("pinkTree",agacresmi)     #resmi bastırma

cv2.waitKey(0)
cv2.destroyAllWindows()