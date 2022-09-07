import numpy as np
import cv2
arr = np.array([[5,7,4],[-1,-7,-4],[-5,1,4]])
img = cv2.imread("F:\Edge ai\images\GFG.png")

fimg = cv2.filter2D(img,-1,arr)
cv2.imshow("img",fimg)
cv2.waitKey(0)