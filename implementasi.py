import cv2 as cv
import numpy as np


def loadimage() :
	image = cv.imread('tengah6.jpg')
	image = cv.GaussianBlur(image, (5,5), 2)

	return image

def convert(image, imtype) :
	if (imtype == 'HSV') :
		image1 = cv.cvtColor(image, cv.COLOR_BGR2HSV)
	elif (imtype == 'YUV') :
		image1 = cv.cvtColor(image, cv.COLOR_BGR2YUV)
	
	return image1

def threshold(image, imtype) :
	lowhsv = np.array([0, 0, 78])
	highhsv = np.array([255, 25, 255])
	lowyuv = np.array([86, 124, 125])
	highyuv = np.array([255, 255, 255]) # parameter didapat dari trackbar

	# threshold process
	if (imtype == 'HSV') :
		im = cv.inRange(image, lowhsv, highhsv)
	elif (imtype == 'YUV') :
		im = cv.inRange(image, lowyuv, highyuv)
	
	return im

def bitwiseops(image1, image2, ops) :
	if (ops == 'AND') :
		combine = np.bitwise_and(image1, image2)
	elif (ops == 'OR') :
		combine = np.bitwise_or(image1, image2)
	elif (ops == 'XOR') :
		combine = np.bitwise_xor(image1, image2)
	
	return combine

def openmorph(image) :
	kernel = np.ones((3, 3), np.uint8)
	image = cv.morphologyEx(image, cv.MORPH_OPEN, kernel)

	return image

def canny(image) :
	canny = cv.Canny(image, 100, 200)
	return canny

def hline(image) :
	lines = cv.HoughLines(image, 1, np.pi/180, 100) # coba diatur lagi jumlah titiknya

def normalisasigaris(lines) (coba di trackbar)
	galatrho = 50
	galatsudut = 0.5
	jumgaris = len(lines)
	erase = [False for i in range(jumgaris)]
	for i in range(jumgaris) :
		if (i != jumgaris - 1) & (not(erase[i])) :		
			for j in range(i+1, jumgaris) :
				if (not(erase[j])) :
					if (abs(lines[i,0,0] - lines[j,0,0]) <= galatrho) :
						erase[j] = True
					if (abs(lines[i,0,1] - lines[j,0,1]) <= galatsudut) :
						erase[j] = erase[j] & True



# line draw
# for i in range(jumgaris) :
#	if (not(erase[i])) :
#		r = lines[i, 0, 0] 
#		sudut = lines[i, 0, 1]
#		x0 = r*(np.cos(sudut))
#		y0 = r*(np.sin(sudut))
#		x1 = int(x0 + 1000*(np.sin(sudut)))
#		y1 = int(y0 - 1000*(np.cos(sudut)))
#		x2 = int(x0 - 1000*(np.sin(sudut)))
#		y2 = int(y0 + 1000*(np.cos(sudut)))

#		cv.line(canny, (x1, y1), (x2, y2), (255, 255, 255), 1)


# contour
im2, contours, hierarchy = cv.findContours(combine, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
cnt = contours[3]
cv.drawContours(image, contours, 0, (0 ,255, 0), 2)
moment = cv.moments(cnt)
area = cv.contourArea(cnt)
cx = int(moment['m10']/moment['m00'])
cy = int(moment['m01']/moment['m00'])
cv.circle(canny, (cx, cy), 2, (255,255,255), 2)
print(area)

# normalisasi data contour berdasarkan luas
cv.imwrite('thresh.jpg', combine)

# showing image
cv.imshow('contour', image)
cv.waitKey(0)
