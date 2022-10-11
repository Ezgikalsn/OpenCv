import cv2
import numpy as np

kamera=cv2.VideoCapture(0)   #Bilgisayar kamerası görüntü almada kullanılacak.

while True:
    ret,goruntu= kamera.read() #her bir frame(kare) aslında resimdir. Resimler doğru okunuyorsa döngüye devam eder.

    cv2.imshow("deneme görüntü",goruntu)

    if cv2.waitKey(30) & 0xFF ==('q'):
        break

kamera.release()

cv2.destroyAllWindows()

