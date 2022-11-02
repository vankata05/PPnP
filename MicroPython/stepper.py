from machine import Pin
from time import sleep_us
import time
class Stepper:
    def __init__(self, stp_, dir_):
        self.stp_ = Pin(stp_, Pin.OUT, value = 0)
        self.dir_ = Pin(dir_, Pin.OUT, value = 0)
        
    def step(self, steps, dir_, time_):
        self.dir_.value(dir_)
        delay = int((time_/steps*500000-420/steps))
        
        for i in range(steps):
            self.stp_.value(1)
            #time/steps/2/10*1000000
            sleep_us(delay)
        
            self.stp_.value(0)
            #time/steps/2/10*9*1000000
            sleep_us(delay)