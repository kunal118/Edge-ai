import cv2
  
  
# # define a video capture object
# vid = cv2.VideoCapture(0)
  
# while(True):
      
#     # Capture the video frame
#     # by frame
#     ret, frame = vid.read()
  
#     # Display the resulting frame
#     cv2.imshow('frame', frame)
      
   
#     cv2.waitKey(1)#waits for 1 ms
  


cam = cv2.VideoCapture(0)


result,i = cam.read()
cv2.imshow("Image",i)

r = cv2.selectROI("Select image area of interest",i)
print(r)
k = cv2.imread("./images/download.png")
resizedK = cv2.resize(k,(r[2],r[3]))
cv2.imshow("Image",resizedK)
i[r[1]:r[1]+r[3],r[0]:r[0]+r[2]] = resizedK;
cv2.imshow("Final",i)
cv2.waitKey(0)

