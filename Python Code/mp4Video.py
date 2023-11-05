import numpy as np
import cv2 as cv
from util import get_limits

from PIL import Image
blue = [255, 0, 0]
cap = cv.VideoCapture("Color Changing Screen Fast Mood Light 1 Hour.mp4")

while cap.isOpened():
    ret, frame = cap.read()
	
    if not ret:
        print("Can't receive frame (stream end?). Ending...")
        break;
    	
    hsvImage = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    	
    lowerLimit, upperLimit = get_limits(color=blue)
    	
    mask = cv.inRange(hsvImage, lowerLimit, upperLimit)
    	
    mask_ = Image.fromarray(mask)

    bbox = mask_.getbbox()

    if bbox is not None:
    	x1, y1, x2, y2 = bbox
    	frame = cv.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 5)
	
    cv.imshow('frame', frame)

    if cv.waitKey(1000//30) == ord('q'):
    	break

cap.release()

cv.destroyAllWindows()

