import cv2
import numpy as np

imagem = cv2.imread('hoo.jpg', cv2.IMREAD_GRAYSCALE)
print(imagem.shape)

cv2.imshow("Hook",imagem)
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

nova1 = mascara(0, 1, 0, 1, -4, 1, 0, 1, 0, imagem, il, ic)
nova2 = mascara(1, 1, 1, 1, -8, 1, 1, 1, 1, imagem, il, ic)
nova3 = mascara(0, -1, 0, -1, 4, -1, 0, -1, 0, imagem, il, ic)
nova4 = mascara(-1, -1,-1,-1, 8, -1, -1, -1, -1, imagem, il, ic)

cv2.imshow("Filtro1",nova1)
cv2.imshow("Filtro2",nova2)
cv2.imshow("Filtro3",nova3)
cv2.imshow("Filtro4",nova4)


cv2.waitKey(0)
cv2.destroyAllWindows()