import cv2
import numpy as np

image = cv2.imread("1.jpg")
print(image.shape)
cv2.imshow("Imagem original",image)
cv2.waitKey(0)
cv2.destroyAllWindows()

il1, ic1, ir1 = image.shape

nova = np.zeros((il1,ic1, ir1), dtype = np.uint8)
nova2 = np.zeros((il1,ic1, ir1), dtype = np.uint8)

for i in range(len(image)):
    for j in range(len(image[0])):
        x = j*(-1)
        nova[i][x][0] = image[i][j][0]
        nova[i][x][1] = image[i][j][1]
        nova[i][x][2] = image[i][j][2]

for i in range(len(image)):
    for j in range(len(image[0])):
        x = i*(-1)
        nova2[x][j][0] = image[i][j][0]
        nova2[x][j][1] = image[i][j][1]
        nova2[x][j][2] = image[i][j][2]

cv2.imshow("Espelho1",nova)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow("Espelho2",nova2)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite("Espelhamento1.jpg",nova)
cv2.imwrite("Espelhamento2.jpg",nova2)