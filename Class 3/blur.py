import cv2
from cv2 import blur
#use of blur to remove noise and augment dataset for noisy images
img = cv2.imread('F:\Edge ai\images\\balloons_noisy.png')
blurIMG = cv2.blur(img,(5,5))
cv2.imshow("OG img",img)
cv2.imshow("Blurred img",blurIMG)
cv2.waitKey(0)



    