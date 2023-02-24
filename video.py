# Capture continuous loop of videos
import time
from picamera2 import Picamera2
from picamera2.encoders import H264Encoder
from picamera2.outputs import FfmpegOutput
from libcamera import controls

# set parameters
fps = 25.0
duration_s = 0.1 * 60
hd_path = "/home/marchmor/Vídeos/"

# initiate camera
picam2 = Picamera2()
picam2.video_configuration.controls.FrameRate = fps
picam2.set_controls({"AfMode": controls.AfModeEnum.Manual, "LensPosition": 0.5}) #1/x, in meters. 0 is infinite
picam2.configure("video")

# capture video continuously
while True:
    # generate file name
    current_time = time.time()
    time_string = time.strftime("%Y%m%d%H%M%S", time.localtime(current_time))
    file_name = hd_path + "video_" + time_string + ".mp4"

    # record video
    picam2.start_and_record_video(file_name, duration = duration_s)
    
    # print name of saved file
    print(f"Saved video as: {file_name}")
