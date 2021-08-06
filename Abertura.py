import cv2
import numpy as np

im_gray = cv2.imread('1.jpg', cv2.IMREAD_GRAYSCALE)
(thresh, image) = cv2.threshold(im_gray, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
print(image.shape)
cv2.imshow("Original em binario",image)
il, ic = image.shape
nova = np.zeros((il,ic), dtype = np.uint8)

for i in range(il):
    for j in range(ic):
        nova.itemset((i ,j),255)


for i in range(il-1):
    for j in range(ic-1):
        if (i is not 0 or j is not 0):
            if(image.item(i - 1, j - 1) == 0 and image.item(i - 1, j) == 0 and image.item(i - 1, j + 1) == 0 and
                    image.item(i, j - 1) == 0 and image.item(i, j)==0 and image.item(i, j + 1)==0 and
                    image.item(i + 1, j - 1) == 0 and image.item(i + 1, j) == 0 and image.item(i + 1, j + 1) == 0):
                nova.itemset((i - 1, j - 1),0)
                nova.itemset((i - 1, j),0)
                nova.itemset((i - 1, j + 1),0)
                nova.itemset((i, j - 1),0)
                nova.itemset((i, j),0)
                nova.itemset((i, j + 1),0)
                nova.itemset((i + 1, j - 1),0)
                nova.itemset((i + 1, j),0)
                nova.itemset((i + 1, j + 1),0)




cv2.imshow("Abertura",nova)
cv2.waitKey(0)
cv2.destroyAllWindows()