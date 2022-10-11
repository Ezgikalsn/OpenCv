import cv2
import numpy as np

Hp=cv2.imread("projeler/HP.png")

sarilanResim=cv2.copyMakeBorder(Hp,50,50,50,50,cv2.BORDER_CONSTANT ,
                                value=(75,150,255)) #hangi resmin uzatılacağını yazdık, üst-alt sağ-sol değerlerini verdik. çerçeve kenarını belirtmek için renk ataması yaptık.

cv2.imshow("Harry Potter",sarilanResim)


cv2.waitKey(0)
cv2.destroyAllWindows()