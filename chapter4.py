import cv2
import  numpy as np
#draw shapes
#define black image
img = np.zeros((512,512, 3))
#add coloring
img[100:300, 50:100] = 255,0,0

#add line
cv2.line(img,(100,100),(300, 300),(255,0,0),3)
cv2.line(img,(100,300), (300,100), (255,0,0),3)
cv2.rectangle(img, (0,0), (img.shape[1], 100), (255,0,255),cv2.FILLED)
cv2.circle(img, (300,300), 50, (255,255,50), 4)
cv2.putText(img, "OPENCV", (20,20), cv2.FONT_HERSHEY_DUPLEX, 1,(255,255,78),2)

cv2.imshow("black canvas", img)
cv2.waitKey(0)