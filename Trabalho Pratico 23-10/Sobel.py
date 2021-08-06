import cv2
import numpy as np

imagem = cv2.imread('Lenna.png', cv2.IMREAD_GRAYSCALE)
print(imagem.shape)

cv2.imshow("Lenna",imagem)
cv2.waitKey(0)
cv2.destroyAllWindows()

il, ic= imagem.shape

def mascara(a,b,c,d,e,f,g,h,i, image, linha, coluna):
    novaimg = np.zeros((linha, coluna), dtype=np.uint8)
    for i1 in range(linha-1):
     for j1 in range(coluna-1):
            if (i1 is not 0 or j1 is not 0):
                aux = ((image.item(i1 - 1, j1 - 1)*a) + (image.item(i1 - 1, j1)*b) + (image.item(i1 - 1, j1 + 1)*c)
                 + (image.item(i1, j1 - 1)*d) + (image.item(i1, j1)*e) + (image.item(i1, j1 + 1)*f)
                 + (image.item(i1 + 1, j1 - 1)*g) + (image.item(i1 + 1, j1)*h) + (image.item(i1 + 1, j1 + 1)*i))
                if(aux<0):
                    aux = 0
                novaimg.itemset((i1, j1), aux)
    return novaimg


h1 = mascara(-1, -2, -1, 0, 0, 0, 1, 2, 1, imagem, il, ic)
h2 = mascara(-1, 0, 1, -2, 0, 2, -1, 0, 1, imagem, il, ic)


cv2.imshow("Detector de Sobel Horizontal",h1)
cv2.imshow("Detector de Sobel Vertical",h2)

soma = np.zeros((il,ic), dtype=np.uint8)

for i in range(il):
    for j in range(ic):
        aux2 = ((h1.item(i, j) + h2.item(i, j)))
        soma.itemset((i, j), aux2)

cv2.imshow("Imagem Gradiente",soma)


cv2.waitKey(0)
cv2.destroyAllWindows()