from machine import Pin
from movement import CoreXY
import _thread
import time

led = Pin("LED", Pin.OUT, value = 1)

mv = CoreXY(0, 0);

mv.g0(200, 220)

#0.9: max steps/s - 20000
#1.8: max steps/s - 10000
    
while 1:
    mv.g0(0, 0)
    time.sleep(0.1)
    mv.g0(220*8, 0)
    time.sleep(0.1)
    #_thread.start_new_thread(trd, ())
    #tmc2209.step(3200, 1, 1)
    #a4988.step(800, 0, 1.17074)
#print(time.ticks_us())