import cv2
cap = cv2.VideoCapture(0)
for i in range(1):
    ret,img = cap.read()
    print(ret)
    cv2.imwrite("my_image.png",img)
del cap

