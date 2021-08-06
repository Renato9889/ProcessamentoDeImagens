import cv2
import numpy as np

imagem = cv2.imread('Lenna.png', cv2.IMREAD_GRAYSCALE)
print(imagem.shape)

cv2.imshow("Lenna",imagem)

il, ic= imagem.shape

for i in range(il):
    for j in range(ic):
        print("%d"%imagem.item(i,j), end = " ")
    print()

cv2.waitKey(0)
cv2.destroyAllWindows()