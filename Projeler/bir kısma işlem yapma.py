import cv2
import numpy as np

resim= cv2.imread("projeler/tree.png")       #resmi okuma
resim[100:450,50:400,0]=255        #sol üst köşeden ağağıya doğru 100-450 arası sağa doğru 50-400 matrislerine mavi rengini verdim 

cv2.imshow("belli bir kısım",resim)     #resmi bastırma

cv2.waitKey(0)
cv2.destroyAllWindows()