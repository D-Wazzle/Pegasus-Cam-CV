import sys
import cv2
import numpy as np
import aruco

if __name__ == '__main__':

	# get camera parameters
	camparam = aruco.getParameters()
	camparam.readFromXMLFile(os.path.join(os.path.dirname(__file__), "dfk72_6mm_param2.yml"))

        # create detector and get parameters
        detector = aruco.MarkerDetector()
        params = detector.getParameters()

        # print detector parameters
        print("detector params:")
        for val in dir(params):
        if not val.startswith("__"):
            print("\t{} : {}".format(val, params.__getattribute__(val)))

	# import Pegasus Cam stream
	cap = cv2.VideoCapture("http://192.168.50.22:3000/html/cam_pic_new.php?time=9999999999999999999999999&pDelay=40000")

	# read a frame from the stream
	ret, frame = cap.read()
	
	# throw error if stream is bad
	if not ret:
		print("Can't open video!")
		sys.exit(-1)

	# while the stream is good
	while ret:
		# get markers in the frame
		markers = detector.detect(frame)
		
		# Print marker coords
		for marker in markers:
			print("Marker: {:d}".format(marker.id))
			for i, point in enumerate(marker):
                		print("\t{:d} {}".format(i, str(point)))
            		marker.draw(frame, np.array([255, 255, 255]), 2)

            		# calculate marker extrinsics for marker size of 3.5cm
            		marker.calculateExtrinsics(0.035, camparam)

            		# print("Marker extrinsics:\n{}\n{}".format(marker.Tvec, marker.Rvec))
            		print("detected ids: {}".format(", ".join(str(m.id) for m in markers)))

        	# show frame
        	cv2.imshow("frame", frame)
        	cv2.waitKey(100)
        
        	# read next frame
        	ret, frame = cap.read()
