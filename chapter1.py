import cv2
import numpy as np

print("package imported")
kernel = np.ones((5,5), np.uint8)


# first read images
#img = cv2.imread("resources/1587631041441.jpg")

# cv2.imshow("Image Box", img)
# cv2.waitKey(0)

# read video files
#cap = cv2.VideoCapture("resources/532.mp4")

#while True:
    #unpacks the read function into two variable, success to store the status of our operation, img to store the video file
#    success, img = cap.read()
#    cv2.imshow('Video box - {}'.format(success), img)
    #if construct to break the initiated loop when the 'q' keyword is pressed
#    if cv2.waitKey(1) & 0xFF == ord('q'):
#        break


#use webcam

#cam = cv2.VideoCapture(0)
#cam.set(3, 640)
#cam.set(4, 480)
#cam.set(10, 100)


#while True:
 #   success, img = cam.read()
  #  cv2.imshow("live camera {}".format(success), img)
   # if cv2.waitKey(1) & 0xFF == ord('q'):
    #    cam.release()
     #   cv2.destroyAllWindows()
      #  break



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
