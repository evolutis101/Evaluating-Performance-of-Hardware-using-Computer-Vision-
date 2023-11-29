import numpy as np
import cv2 as cv
import sys

import time
import psutil

from PIL import Image

from util import get_limits

yellow = [0, 255, 255]

start_time = time.time() #start measuring execution time

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

end_time = time.time() #end measuring execution time
execution_time = end_time - start_time
cpu_usage = psutil.cpu_percent(interval=1) #measure cpu usage
memory_usage = psutil.virtual_memory().percent #measure memory usage
   
#print the performance metrics
print(f"Execution Time: {execution_time:.2f} seconds")
print(f"CPU Usage: {cpu_usage:.2f}%")
print(f"Memory Usage: {memory_usage:.2f}%")

k = cv.waitKey(1000)
