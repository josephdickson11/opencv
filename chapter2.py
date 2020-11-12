import  cv2
import numpy as np

kernel = np.ones((5,5), np.uint8)


#   basic functionalities
# 1- imageto gray

img = cv2.imread("resources/1587631041441.jpg")
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#add blur
img_blur = cv2.GaussianBlur(img, (11,11), 0)
#add edge detection
img_canny = cv2.Canny(img_gray, 30, 30)
#add image dialation
img_dialate = cv2.dilate(img_canny, kernel,iterations=1)
#add image erosion
img_erode = cv2.erode(img_dialate, kernel, iterations=1)

cv2.imshow("gray image", img_gray)
cv2.imshow("blur image", img_blur)
cv2.imshow("edge image", img_canny)
cv2.imshow("dialated image", img_dialate)
cv2.imshow("eroded Image", img_erode)


cv2.waitKey(0)
