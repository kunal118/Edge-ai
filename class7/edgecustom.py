import cv2
import numpy as np
vid = cv2.VideoCapture(0)
arr = np.array([[5,7,4],[-1,-7,-4],[-5,1,4]])
while(True):
      
    # Capture the video frame
    # by frame
    ret, frame = vid.read()
  
    # Display the resulting frame
    gray = cv2.cvtColor(frame   , cv2.COLOR_BGR2GRAY)
    frame_edge = cv2.filter2D(gray,0,arr)
    cv2.imshow("video",np.uint8(frame_edge)); 
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()