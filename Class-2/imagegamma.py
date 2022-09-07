import numpy as np
import cv2

def gamma_coorection(image,gamma):
    gamma = 1/gamma
    table = np.array([((1/255)**gamma)*255 for i in np.arange(0,256)]).astype()
