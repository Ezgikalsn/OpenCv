import cv2
import numpy as np

Hp=cv2.imread("projeler/HP.png")

uzatilanResim=cv2.copyMakeBorder(Hp,200,600,300,300,cv2.BORDER_REPLICATE) #hangi resmin uzatılacağını yazdık, üst-alt sağ-sol değerlerini verdik. 

cv2.imshow("Harry Potter",uzatilanResim)

cv2.waitKey(0)
cv2.destroyAllWindows()