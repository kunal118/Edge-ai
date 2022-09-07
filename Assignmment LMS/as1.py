import cv2
import numpy as np
from matplotlib import pyplot as plt

face_classifier = cv2.CascadeClassifier('F:\Edge ai\class 4\haarcascade_frontalface_default.xml')
object = cv2.imread("F:\Edge ai\images\img1.png")
vid = cv2.VideoCapture(0)
  
while(True):
      
    # Capture the video frame
    # by frame
    ret, frame = vid.read()
  
    # Display the resulting frame
    gray = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray, 1.3, 5) 
    for (x,y,w,h) in faces:
        
        
        
        resizedObj = cv2.resize(object,(w,h))
        
        frame[y:y+h, x:x+w] = resizedObj
        
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
    cv2.imshow('frame', frame)
    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()