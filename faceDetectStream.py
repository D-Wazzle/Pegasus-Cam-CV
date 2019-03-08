import numpy as np
import cv2
from datetime import datetime

# import Haar cascades
face_cascade = cv2.CascadeClassifier('/usr/local/share/OpenCV/haarcascades/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('/usr/local/share/OpenCV/haarcascades/haarcascade_eye.xml')

# import Pegasus Cam stream
cap = cv2.VideoCapture("http://192.168.50.22:3000/html/cam_pic_new.php?time=9999999999999&pDelay=40000")

# while the stream is good
while(cap.isOpened()):

	# get current time
	time_1 = datetime.now()
	print(time_1)

	# get current frame
	ret, frame = cap.read()

	# convert ot grayscale
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	# detect faces in the frame
	faces = face_cascade.detectMultiScale(gray, 1.3, 5)

	# display bounding boxes for face features
	for(x, y, w, h) in faces:
		cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), -1)
		roi_gray = gray[y:y+h, x:x+w]
		roi_color = frame[y:y+h, x:x+w]
		eyes = eye_cascade.detectMultiScale(roi_gray)
		# dispay bounding boxes for eyes
		for(ex, ey, ew, eh) in eyes:
			cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)

	cv2.imshow('frame', frame)


	# get elapsed time
	time_2 = datetime.now()
	dt = time_2 - time_1
	print(dt.seconds*1000 + dt.microseconds/1000)

	# wait for ESC key to exit
	k = cv2.waitKey(10)
	if k == 27:
    		cv2.destroyAllWindows()

cap.release()
cv2.destroyAllWindows()
