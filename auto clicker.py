import ctypes
import time
# see http://msdn.microsoft.com/en-us/library/ms646260(VS.85).aspx for details
time.sleep(3)
for x in range(2000):
    ctypes.windll.user32.mouse_event(2, 0, 0, 0,0) # left down
    #time.sleep(.005)
    ctypes.windll.user32.mouse_event(4, 0, 0, 0,0) # left up
    time.sleep(.00825)
