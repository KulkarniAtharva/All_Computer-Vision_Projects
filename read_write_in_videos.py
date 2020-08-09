import cv2

cap = cv2.videoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc,20.0,(640,480))

if not cap.isOpened():
	print("Cannot open Camera")
	exit()

while (True):				# while(cap.isOpened())
	ret,frame = cap.read()		# Capture frame-by-frame

	if not ret:
		print("Can't receive frame(stream end ?). Exiting.....")
		break

	frame = cv.flip(frame, 0)

	 out.write(frame)	# write the flipped frame

	 print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
	 print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

	 cap.set(3,1208)   # 3 is property for width indicates width 
	 cap.set(4, 720)   # 4 is property for height indicates height

"""
	I can check the frame width and height by cap.get(cv.CAP_PROP_FRAME_WIDTH) and cap.get(cv.CAP_PROP_FRAME_HEIGHT). 
	It gives me 640x480 by default. But I want to modify it to 320x240. Just use ret = cap.set(cv.CAP_PROP_FRAME_WIDTH,320) and ret = cap.set(cv.CAP_PROP_FRAME_HEIGHT,240).
"""

	

	# Show date and time on video 
	font = cv2.FONT_HERSHEY_SIMPLEX
	text = 'Width: '+str(cap.get(3))+'Height: '+str(cap.get(4))
	datet = str(datetime.datetime.now())
	frame = cv2.putText(frame,datet,(10,50),font,1,(0,255,255),2,cv2.LINE_AA)


	gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

	cv2.imshow('frame',frame)

	if(cv2.waitKey(1) & 0xFF == ord("q")):
		break

cap.release()
out.release()
cv2.destroyAllWindows()