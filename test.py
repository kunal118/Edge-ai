
import cv2
from PIL import Image
from torchvision.transforms import transforms
#for image transformations like normalisation of intensity etc 

transform = transforms.Compose([transforms.ToTensor()])
i = cv2.imread('./img1.png')
print(i.shape)
# (250, 248, 3)
# 3 color layers r g b

# for grayscale image it outputs a 2d matrix
i = cv2.imread('./img1.png',0)
print(i.shape)


#Reading image using pillow
j = Image.open('./img1.png')
# print(j.shape) 

#  gives error as it rturns image object and not a 
jArray = transform(j)
print(jArray.shape)

print(type(jArray))



# Net output till now
# (250, 248, 3)
# (250, 248)
# torch.Size([4, 250, 248])

# Difference in way it  displays dimensions



# ................................................................................
# ................................................................................
# ................................................................................

# Recolor a selected region of a image
r = cv2.selectROI("Select image area of interest",i)
# left top width height
print(r)
