import cv2
import numpy as np

Hp=cv2.imread("projeler/HP.png")

aynalananResim=cv2.copyMakeBorder(Hp,300,300,300,300,cv2.BORDER_REFLECT) #hangi resmin aynalanacağını yazdık, üst-alt sağ-sol değerlerini verdik. 

cv2.imshow("Harry Potter",aynalananResim)

cv2.waitKey(0)
cv2.destroyAllWindows()