import cv2
import numpy as np
from matplotlib import pyplot as plt

face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

i=cv2.imread('F:\Edge ai\images\\face.jpg')
gray = cv2.imread('F:\Edge ai\images\\face.jpg',0)

cv2.imshow('img',gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
plt.figure()
plt.imshow(i)
plt.title('my picture')
plt.show()
faces = face_classifier.detectMultiScale(gray, 1.3, 5) 
for (x,y,w,h) in faces:
    i = cv2.rectangle(i,(x,y),(x+w,y+h),(255,0,0),2) 
    roi_gray = gray[y:y+h, x:x+w] 
    roi_color = i[y:y+h, x:x+w]

    plt.figure()
    plt.imshow(i) 
    plt.title('my picture') 
    plt.show()