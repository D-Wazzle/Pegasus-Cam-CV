import numpy as np
import cv2
from datetime import datetime

#fourcc = cv2.VideoWriter_fourcc(*'XVID')
#out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

cap = cv2.VideoCapture("http://192.168.50.21:80/html/cam_pic_new.php?time=9999999999999&pDelay=40000")

while(cap.isOpened()):
	time_1 = datetime.now()

	ret, frame = cap.read()

	gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

	cv2.imshow('frame', gray)

	#out.write(frame)

	time_2 = datetime.now()
	dt = time_2 - time_1
	print(dt.microseconds)

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
#out.release()
cv2.destroyAllWindows()
