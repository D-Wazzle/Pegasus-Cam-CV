import numpy as np
import cv2
from datetime import datetime

#fourcc = cv2.VideoWriter_fourcc(*'XVID')
#out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

face_cascade = cv2.CascadeClassifier('/usr/local/share/OpenCV/haarcascades/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('/usr/local/share/OpenCV/haarcascades/haarcascade_eye.xml')

cap = cv2.VideoCapture("http://192.168.50.22:3000/html/cam_pic_new.php?time=9999999999999&pDelay=40000")

while(cap.isOpened()):
	time_1 = datetime.now()
	print(time_1)

	ret, frame = cap.read()

	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	faces = face_cascade.detectMultiScale(gray, 1.3, 5)
	for(x, y, w, h) in faces:
		cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), -1)
		roi_gray = gray[y:y+h, x:x+w]
		roi_color = frame[y:y+h, x:x+w]
		eyes = eye_cascade.detectMultiScale(roi_gray)
		for(ex, ey, ew, eh) in eyes:
			cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)

	cv2.imshow('frame', frame)

	#out.write(frame)

	time_2 = datetime.now()
	dt = time_2 - time_1
	print(dt.seconds*1000 + dt.microseconds/1000)

	k = cv2.waitKey(10)
	if k == 27:         # wait for ESC key to exit
    		cv2.destroyAllWindows()

cap.release()
#out.release()
cv2.destroyAllWindows()
