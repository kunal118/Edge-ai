import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread("F:\Edge ai\images\sudoku-puzzle.jpg")

rows,columns,c = img.shape

plt.imshow(img)
x = plt.ginput(4)#takes 4 input graphical points
print(x)
plt.show()

pts1 = np.float32([x[0],x[1],x[2],x[3]])
pts2 = np.float32([[0,0],[columns,0],[columns,rows],[0,rows]])

A = cv2.getPerspectiveTransform(pts1,pts2)
transformedImg = cv2.warpPerspective(img,A,(columns,rows))

plt.subplot(1, 2, 1)
plt.imshow(img)
plt.subplot(1, 2, 2)
plt.imshow(transformedImg)
plt.show()



