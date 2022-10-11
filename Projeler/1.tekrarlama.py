import cv2
import numpy as np

Hp=cv2.imread("projeler/HP.png")

tekrarResim=cv2.copyMakeBorder(Hp,200,600,300,300,cv2.BORDER_WRAP) #hangi resmin tekrarlanacağını yazdık, üst-alt sağ-sol değerlerini verdik. 

cv2.imshow("Harry Potter",tekrarResim)

cv2.waitKey(0)
cv2.destroyAllWindows()