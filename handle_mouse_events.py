import numpy as np
import cv2

#events = [i for i in dir(cv2) if 'EVENT' in i]    # for listing out the events
#print(events)

def click_event(event,x,y,flag,param):
	if event == cv2.EVENT_LBUTTONDOWN:
		print(x,',',y)
		font = cv2.FONT_HERSHEY_SIMPLEX
		strXY = str(x)+', '+str(y)
		cv2.putText(img,strXY,(x,y),font,1,(255,255,0),2)		# image,string,font,font scale,color,thickness
		cv2.imshow('image',img)

	if event == cv2.EVENT_RBUTTONDOWN:
		blue = img[y,x,0]   # 0 channel for blue
		green = img[y,x,1]   # 0 channel for green
		red = img[y,x,2]   # 0 channel for red
		font = cv2.FONT_HERSHEY_SIMPLEX
		strBGR = str(blue)+', '+str(green)+', '+str(red)
		cv2.putText(img,strBGR,(x,y),font,.5,(255,255,0),2)
		cv2.imshow('image',img)



img = np.zeros((512,512,3),np.uint8)
# img = cv2.imread('a.png')		# if you want the output on a image instead of a black screen


cv2.imshow('image',img)

cv2.setMouseCallback('image',click_event)

cv2.waitKey(0)
cv2.destroyAllWindows() 