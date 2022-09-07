# Recolor a selected region of a image

from turtle import down
import cv2

i = cv2.imread('F:\Edge ai\images\img1.png')
# print(i.shape)

r = cv2.selectROI("Select image area of interest",i)
# left top width height (21, 30, 97, 100)
print(r)

# Recolor a selected region of a image
i[r[1]:r[1]+r[3],r[0]:r[0]+r[2],0] = 0 #blue
i[r[1]:r[1]+r[3],r[0]:r[0]+r[2],1] = 0 #green
i[r[1]:r[1]+r[3],r[0]:r[0]+r[2],2] = 255 #red

cv2.imshow("Modified image",i)

k=cv2.imread("./download.png")
cv2.imshow("image",k)
cv2.waitKey(0)
resizedK = cv2.resize(k,(r[2],r[3]))
i[r[1]:r[1]+r[3],r[0]:r[0]+r[2]] =  resizedK

cv2.imshow("Modified image 2",i)
cv2.waitKey(0)





