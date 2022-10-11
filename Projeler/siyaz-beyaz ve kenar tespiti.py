import cv2
import numpy as np

resim= cv2.imread("projeler/tree.png")    # resmi okuma
gray=cv2.cvtColor(resim, cv2.COLOR_BGR2GRAY)   # resmi siyah-beyaz yapma
blur=cv2.GaussianBlur(gray,(7,7),0)  #görüntüdeki pürüzlerden kurtulmak için blurlama işlemi

canny=cv2.Canny(blur,50,150)  #kenar belirleme

cv2.imshow("blurred resim", blur)
cv2.imshow("canny resim", canny)

cv2.waitKey(0)
cv2.destroyAllWindows()