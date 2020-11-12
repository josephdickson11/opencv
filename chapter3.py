import cv2
import numpy as np

kernel = np.ones((5,5), np.uint8)

img = cv2.imread("resources/1591988497278.jpg")
print(img.shape)
edge_img = cv2.Canny(img, 30, 30)
resize_img = cv2.resize(img,(300, 200))
cropped_img = img[:200, :200]

cv2.imshow("image box", img)
cv2.imshow("edge image", edge_img)
cv2.imshow("resized image", resize_img)
cv2.imshow("croppeed image", cropped_img)
print(edge_img.shape)

cv2.waitKey(0)