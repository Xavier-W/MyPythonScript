import cv2

cap = cv2.VideoCapture()
ret, frame = cap.read()
i=0
if ret==1:
    cv2.imwrite('D:/'+str(i)+'.jpg', frame)


