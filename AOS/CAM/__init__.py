import multiprocessing
import time
from CameraControl import CameraControl
from Undistort import Undistort


#set up a queue and events to communicate with the camera process
frame_queue, camera_process_event, get_frames_event = multiprocessing.Queue(maxsize=1000), multiprocessing.Event(), multiprocessing.Event()

# init a camera class
camera_class = CameraControl()

# init the undistortion class
ud = Undistort()

#start the camera_process as a separate process
camera_process = multiprocessing.Process(name = 'camera_process',target=camera_class.AcquireFrames, args=(frame_queue, camera_process_event, get_frames_event))
camera_process.start()

# Start recording by sending an event signal 
get_frames_event.set()

# ...

# Retrieve recorded frames
frames_info = frame_queue.get()
# frames_info is dictionary of the form { 'Frames': [img1, img2, ...] 'FrameTimes': [time1, time2, ...] }
times = frames_info['FrameTimes']

# undistort the recorded frames
for image in frames_info['Frames']:
    undistored = ud.undistort( image )

# Stop recording by sending an event
camera_process_event.set()

# cleanup
frame_queue.close()
camera_process.join(5) 
if camera_process.is_alive() :
    camera_process.terminate()
