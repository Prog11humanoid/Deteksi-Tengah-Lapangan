import cv2 as cv
import numpy as np

gambar = cv.imread('thresh.jpg')

gambar = cv.cvtColor(gambar, cv.COLOR_BGR2GRAY)

im2, contours, hierarchy = cv.findContours(gambar, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

# print(len(contours))
cv.drawContours(gambar, contours, -1, (255,255,255), 2)

cv.imshow('ellips', gambar)

cv.waitKey(0)
