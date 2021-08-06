import cv2
import numpy as np
imagem = cv2.imread('frozen.jpg', cv2.IMREAD_GRAYSCALE)
print(imagem.shape)

cv2.imshow("Original",imagem)
cv2.waitKey(0)
cv2.destroyAllWindows()

il1, ic1 = imagem.shape

nova = np.zeros((il1,ic1), dtype = np.uint8)
nova2 = np.zeros((il1,ic1), dtype = np.uint8)
aux1 = 0
for i in range(il1):
    for j in range(ic1):
        aux2 = imagem[i][j]
        if aux1<aux2:
            aux1 = aux2

for i in range(il1):
    for j in range(ic1):
       nova[i][j] = aux1 - (imagem[i][j]-1)

for i in range(il1):
    for j in range(ic1):
        aux3 = pow(imagem[i][j]/255,0.3)
        nova2[i][j] = round(aux3*255)

cv2.imshow("Negativa",nova)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow("Gama",nova2)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite("Negativa.jpg",nova)
cv2.imwrite("Gama.jpg",nova2)