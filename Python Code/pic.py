import cv2 as cv
from PIL import Image

from util import get_limits

yellow = [0, 255, 255]

img = cv.imread('lemon.jpg')

if img is None:
	sys.exit("could not read the image.")

hsvImage = cv.cvtColor(img, cv.COLOR_BGR2HSV)

lowerLimit, upperLimit = get_limits(color=yellow)

mask = cv.inRange(hsvImage, lowerLimit, upperLimit)

mask_ = Image.fromarray(mask)

bbox = mask_.getbbox()

if bbox is not None:
	x1, y1, x2, y2 = bbox
	
	img = cv.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 5)

cv.imshow('Display window', img)

k = cv.waitKey(0)
