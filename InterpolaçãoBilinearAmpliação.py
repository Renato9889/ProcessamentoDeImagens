import cv2
import numpy as np

image = cv2.imread("frozen.jpg")
print(image.shape)

cv2.imshow("Frozen",image)
cv2.waitKey(0)
cv2.destroyAllWindows()

il, ic, ir = image.shape

nova = np.zeros((2 * il, 2 * ic, ir), dtype = np.uint8)
for i in range(il):
    for j in range(ic):
        for d in range(ir):
            nova.itemset((i*2,j*2,d), image.item(i,j,d))


for i in range(il*2 - 1):
    for j in range(ic*2 -1):
        for d in range(ir):
           if i%2 == 0 and j%2 == 0:
               continue
           else:
               if i%2 == 0 and j%2 !=0:
                   aux = (nova.item(i,j + 1, d)+nova.item(i,j - 1, d))//2
                   nova.itemset((i,j,d), aux)
               else:
                   if i%2 != 0 and j%2 ==0:
                       aux = (nova.item(i+1,j + 1, d)+nova.item(i-1,j, d))//2
                       nova.itemset((i, j, d), aux)
                   else:
                       (nova.item(i + 1, j + 1, d) + nova.item(i - 1, j - 1, d)) // 4
                       nova.itemset((i, j, d),aux)

print(nova.shape)
cv2.imshow("Frozen",nova)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite("ImagemAmpliadaBilinear.jpg",nova)