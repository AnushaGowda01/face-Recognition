# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 15:11:16 2020

@author: admin
"""

import numpy as np
import cv2
import pyttsx3
face_cascade = cv2.CascadeClassifier("C:/Users/Anusha/Documents/face_Recog1/haarcascade_frontalface_default.xml")

cap = cv2.VideoCapture(0)
rec = cv2.face.LBPHFaceRecognizer_create()
rec.read("C:/Users/Anusha/Documents/face_Recog1/trainingdata.yml")

id=0

while 1:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.5, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        id,conf=rec.predict(gray[y:y+h,x:x+w])
        
        if(id==1):
            print("Anusha")
            pyttsx3.speak("this is anusha")
        elif(id==4):
            print("Sangeetha")
            pyttsx3.speak("this is sangeetha")
        elif(id==3):
            print("Mahalakshmi")
            pyttsx3.speak("this is Mahalakshmi")
 
    cv2.imshow('img',img)
    
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()