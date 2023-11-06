import cv2
import time
import psutil
from PIL import Image
from util import get_limits

yellow = [255, 0, 0]  # blue
cap = cv2.VideoCapture(0)
start_time = time.time() #start measuring execution time
end_time = start_time + 30 #run for 30 seconds
while time.time() < end_time:

    ret, frame = cap.read()

    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lowerLimit, upperLimit = get_limits(color=yellow)

    mask = cv2.inRange(hsvImage, lowerLimit, upperLimit)

    mask_ = Image.fromarray(mask)

    bbox = mask_.getbbox()

    if bbox is not None:
        x1, y1, x2, y2 = bbox

        frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 5)		

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
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
cv2.destroyAllWindows()

