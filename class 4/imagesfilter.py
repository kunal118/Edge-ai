import cv2
from PIL import Image,ImageFilter


#use of blur to remove noise and augment dataset for noisy images

i = Image.open('F:\Edge ai\images\\balloons_noisy.png')
i.filter(ImageFilter.MinFilter(size=5))
i.show()






    