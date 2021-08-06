import cv2
import numpy as np

image = cv2.imread("frozen.jpg")
print(image.shape)

cv2.imshow("Frozen",image)
cv2.waitKey(0)
cv2.destroyAllWindows()

il, ic, ir = image.shape

nova = np.zeros((il//2,ic//2, ir), dtype = np.uint8)
for i in range(il//2):
    for j in range(ic//2):
        for d in range(ir):
            aux  = (image.item(i*2,j*2, d)+image.item(i*2,j*2+1, d)+image.item(i*2+1,j*2, d)+image.item(i*2+1,j*2+1, d))//4
            nova.itemset((i, j, d),aux)
print(nova.shape)
cv2.imshow("Frozen",nova)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite("ImagemReduzidaBilinear.jpg",nova)