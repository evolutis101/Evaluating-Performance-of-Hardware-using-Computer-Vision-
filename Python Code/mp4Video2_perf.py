import numpy as np
import cv2 as cv

#i added this
import time
import psutil

from util import get_limits
from PIL import Image
blue = [255, 0, 0]
cap = cv.VideoCapture("Color Changing Screen Fast Mood Light 1 Hour.mp4")

start_time = time.time() #start measuring execution time
end_time = start_time + 30 #run for 30 seconds

while time.time() < end_time:
    
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
    	
end_time = time.time() #end measuring execution time
execution_time = end_time - start_time
cpu_usage = psutil.cpu_percent(interval=1) #measure cpu usage
memory_usage = psutil.virtual_memory().percent #measure memory usage
   
#print the performance metrics
print(f"Execution Time: {execution_time:.2f} seconds")
print(f"CPU Usage: {cpu_usage:.2f}%")
print(f"Memory Usage: {memory_usage:.2f}%")

cap.release()

cv.destroyAllWindows()
