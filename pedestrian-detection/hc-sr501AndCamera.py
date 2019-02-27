from gpiozero import MotionSensor
from picamera import PiCamera
import time
import datetime
import os 
pir=MotionSensor(4)
camera=PiCamera()
def getFilename():
    return datetime.datetime.now().strftime("images/images.jpg")
while True:
    filename=getFilename()
    pir.wait_for_motion()
    if pir.motion_detected:
        print("Hareket Algılandı")
        camera.start_preview()
        camera.capture(filename)
        camera.stop_preview()
        time.sleep(1)
    os.system("python3 /home/pi/pedestrian-detection/deep_learning_object_detection.py")
        
