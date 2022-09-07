import cv2

i = cv2.imread("./background1.jpg")
car = cv2.imread("./car1.png")
print(int(i.shape[0]/10),int(i.shape[1]/10))
car = cv2.resize(car,(200,100))
cv2.imshow("image1",car)


cv2.waitKey(0)

print(cv2.__dict__)


