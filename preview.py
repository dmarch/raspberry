# Preview camera
# Use this preview to help placing the camera in the right position
from picamera2 import Picamera2
from libcamera import controls
import time
picam2 = Picamera2()
picam2.start(show_preview=True)
picam2.set_controls({"AfMode": controls.AfModeEnum.Manual, "LensPosition": 0.5}) #1/x, in meters. 0 is infinite
#time.sleep(5)  # preview time, in seconds
#picam2.stop()
