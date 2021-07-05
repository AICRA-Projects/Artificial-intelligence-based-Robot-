import numpy as np
import cv2

hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
#cv2.startWindowThread()
cap = cv2.VideoCapture(0)
while(True):
	ret, frame = cap.read()
	frame = cv2.resize(frame, (640,460))
	gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
	box, weights = hog.detectMultiScale(frame, winStride=(8,8))
	box = np.array([[x, y, x+w, y+h] for (x,y,w,h) in box])
	for xa,ya,wa,ha in box:
		cv2.rectangle(frame, (xa,ya),(wa,ha),(0, 255, 0), 2)
	cv2.imshow('frame',frame)
	if cv2.waitKey(1) & 0xFF== ord('q'):
		break

cap.release() 
cv2.destroyAllWindows()
cv2.waitKey(1)
