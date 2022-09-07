from cv2 import log
import numpy as np
import cv2
import math
import imutils



def gamma_corr(image,gamma):

    invGamma = 1.0/gamma
    table = np.array([((i/255.0)**invGamma)*255 for i in np.arange(0,256)]).astype("uint8")

    return cv2.LUT(image,table)

def log_transform(image,c):
    # c = 255 / np.log(1 + np.max(image))
    # log_image = c * (np.log(image + 1)).astype("uint8")
    table = np.array([c*255*(np.log((i/255.0)+1)) for i in np.arange(0,256)]).astype("uint8")

    return cv2.LUT(image,table)

def illumination(image,c):
    return np.uint8(image*c)

img = cv2.imread("F:\Edge ai\images\\nature.jpg")
# cv2.imshow("original Image",img)
# cv2.waitKey(0)

# gammaimg = gamma_corr(img,0.5)
# cv2.imshow("gamma Image 0.5",gammaimg)
# cv2.waitKey(0)

logtransform = log_transform(img,2)
cv2.imshow("log transformed",logtransform)
cv2.waitKey(0)

print(cv2.__dict__)

# illuminatedimg = illumination(img,5)
# cv2.imshow("illuminated img",illuminatedimg)
# print(illuminatedimg[0][0])
# cv2.waitKey(0)

# rotatedimage = imutils.rotate_bound(img,30)
# cv2.imshow("Rotated image",rotatedimage)
# cv2.waitKey(0)

