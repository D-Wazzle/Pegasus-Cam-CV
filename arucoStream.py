import sys
import cv2
import numpy as np
import aruco

if __name__ == '__main__':

	camparam = aruco.getParameters()
	camparam.readFromXMLFile(dfk

	cap = cv2.VideoCapture("http://192.168.50.22:3000/html/cam_pic_new.php?time=9999999999999999999999999&pDelay=40000")

	ret, frame = cap.read()
	
	if not ret:
		print("Can't open video!")
		sys.exit(-1)

	while ret:
		markers = detector.detect(frame)
		
		for marker in markers:
			print("Marker: {:d}".format(marker.id))	
