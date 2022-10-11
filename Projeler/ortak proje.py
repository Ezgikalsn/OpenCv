import cv2

def nothing(x):
    pass
cv2.namedWindow("webcam")    #kameradan alınacak görüntünün açılan penceredeki ismi
cv2.createTrackbar("L_TH","webcam",0,255,nothing)   # 0-255 arasında değerler verebileğimiz trackbar 
cv2.createTrackbar("U_TH","webcam",0,255,nothing)   # 0-255 arasında değerler verebileğimiz trackbar 
cv2.setTrackbarPos("U_TH","webcam",255)
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)   #Bilgisayar kamerasından görüntü alma

while True:
    ret, frame = cap.read()  #her bir frame(kare) aslında resimdir. Resimler doğru okunuyorsa döngüye devam eder.
    if ret == 0:
        break  #resimler yanlış okunuyorsa kameradan görüntü almayı bırakır.
    frame = cv2.flip(frame, 1)  #görüntüyü çevirme
    frame_gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)  #görüntüyü siyah-beyaz yapma
    frame_gray = cv2.GaussianBlur(frame_gray,(5,5),0)   #görüntüdeki pürüzlerden kurtulmak için blurlama işlemi
    uth = cv2.getTrackbarPos("U_TH","webcam")
    lth = cv2.getTrackbarPos("L_TH","webcam")
    canny = cv2.Canny(frame_gray,lth,uth)  #kenar belirleme
    cv2.imshow("webcam", canny)   #görüntüyü bastırma
    if cv2.waitKey(36) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
