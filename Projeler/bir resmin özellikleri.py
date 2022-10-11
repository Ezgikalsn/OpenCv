import cv2
import numpy as np

resim = cv2.imread("projeler/yol bulma.png")   #Resmi okuma 

cv2.imshow("deneme",resim) #Resmi bastırma

print(resim[(15,20)])  #Parantez içine yazdığımızın matrisin BGR karşılığını bulma

print("Resmin boyutu: " +str(resim.size))  
print("Resmin özellikleri:" +str(resim.shape))
print("Resmin veri tipi: " +str(resim.dtype))

cv2.waitKey(0)
cv2.destroyAllWindows()