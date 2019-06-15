import cv2 as cv
import numpy as np

def nothing(x):
	pass


a = cv.imread('tengah4.jpg')
cv.namedWindow('PARAM')
cv.createTrackbar('hMin','PARAM', 0, 255, nothing)
cv.createTrackbar('hMax','PARAM', 255, 255, nothing)
cv.createTrackbar('sMin','PARAM', 0, 255, nothing)
cv.createTrackbar('sMax','PARAM', 255, 255, nothing)
cv.createTrackbar('vMin','PARAM', 0, 255, nothing)
cv.createTrackbar('vMax','PARAM', 255, 255, nothing)
while(True):
	gray = cv.cvtColor(a, cv.COLOR_BGR2HSV)
	blur = cv.GaussianBlur(gray,(5,5),2)
	hMin = cv.getTrackbarPos('hMin', 'PARAM')
	hMax = cv.getTrackbarPos('hMax', 'PARAM')
	sMin = cv.getTrackbarPos('sMin', 'PARAM')
	sMax = cv.getTrackbarPos('sMax', 'PARAM')
	vMin = cv.getTrackbarPos('vMin', 'PARAM')
	vMax = cv.getTrackbarPos('vMax', 'PARAM')
	lower = np.array([hMin, sMin, vMin])
	upper = np.array([hMax, sMax, vMax])
	#print(lower)
	threshold = cv.inRange(blur, lower, upper)	
	cv.imshow('image1', gray)
	cv.imshow('image2', threshold)
	if(cv.waitKey(1) & 0xFF == ord('q')):
		break

cap.release()
cv.destroyAllWindows()
