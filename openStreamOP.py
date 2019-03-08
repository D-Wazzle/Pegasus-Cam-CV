import numpy as np
import cv2

#fourcc = cv2.VideoWriter_fourcc(*'XVID')
#out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

cap = cv2.VideoCapture("http://192.168.50.20:3000/html/cam_pic_new.php?time=9999999999999&pDelay=40000")

while(cap.isOpened()):
	ret, frame = cap.read()

	gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

	cv2.imshow('frame', gray)

	#out.write(frame)

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
#out.release()
cv2.destroyAllWindows()
