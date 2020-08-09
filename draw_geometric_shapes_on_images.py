import numpy as  np
import cv2

#img = cv2.imread("a.png",0)  # 0 bcoz reading in grayscale format
img = np.zeros([512,512,3],np.uint8)

img = cv2.line(img,(0,0),(255,255),(255,0,0),5)		#  image,start,end,color,thickness   # Blue (255,0,0)
img = cv2.arrowedLine(img,(0,255),(255,255),(255,0,0),10)


img = cv2.rectangle(img,(384,0),(510,128),(0,0,255),5)			# if thickness is -1 intead of 5 then we get a filled rectangle
img = cv2.circle(img,(447,63),63,(0,255,0),-1)

font = cv2.FONT_HERSHEY_SIMPLEX
img = cv2.putText(img,'OpenCV',(10,500),font,4,(255,255,255),10,cv2.LINE_AA)

cv2.imshow('image',img)

cv2.waitKey(0)
cv2.destroyAllWindows()