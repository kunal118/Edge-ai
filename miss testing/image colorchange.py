import cv2

i= cv2.imread('F:\Edge ai\miss testing\introImg.jpg');
igray = cv2.imread('F:\Edge ai\miss testing\introImg.jpg',0);
print(i.shape)
print(igray)
for j in range(i.shape[0]):
    print(int(j/45))
    for k in range(i.shape[1]):
        
        if(igray[j][k] == 255):
            # print(i[j][k])
            i[j][k] = (41, 37,33)
            # print(i[j][k])

cv2.imwrite("F:\Edge ai\miss testing\introtransformImg.jpg",i)
