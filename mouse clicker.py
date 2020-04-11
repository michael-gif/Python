import ctypes
import time
time.sleep(3)
for x in range(260):
    ctypes.windll.user32.mouse_event(2, 0, 0, 0,0) # left down
    ctypes.windll.user32.mouse_event(4, 0, 0, 0,0) # left up
    time.sleep(.03778)