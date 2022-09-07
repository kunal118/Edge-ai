from matplotlib.pyplot import new_figure_manager
import imutils
import cv2 as cv
import numpy as np

i=cv.imread('F:\Edge ai\images\\nature.jpg')
alpha=1.04

c=1

for beta in range(25):
    new_image=cv.convertScaleAbs(i,alpha=alpha,beta=beta)
    cv.imwrite('aug/'+str(c)+'.jpg',new_image)
    c+=1

ii=1

for r in np.linspace(-10,10,91):
    rotated=imutils.rotate_bound(i,r)
    cv.imwrite('F:\Edge ai\Class 3\\aug/'+str(ii)+'.jpg',rotated)
    ii=ii+1;