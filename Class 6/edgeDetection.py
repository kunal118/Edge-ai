import cv2
import numpy as np
vid = cv2.VideoCapture(0)
  
while(True):
      
    # Capture the video frame
    # by frame
    ret, frame = vid.read()
  
    # Display the resulting frame
    gray = cv2.cvtColor(frame   , cv2.COLOR_BGR2GRAY)
    frame_edge = cv2.Sobel(gray,cv2.CV_8U,1,1,ksize=3)
    cv2.imshow("video",np.uint8(255-frame_edge)); 
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()