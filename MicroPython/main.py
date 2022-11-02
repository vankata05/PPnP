from machine import Pin
from machine import PWM
from time import sleep
import time

from stepper import Stepper

led = Pin("LED", Pin.OUT, value = 1)

tmc2209 = Stepper(18, 19)
a4988 = Stepper(17, 16)

print(time.ticks_us())

#0.9: max steps/s - 20000
#1.8: max steps/s - 10000
while 1:
    tmc2209.step(3200, 1, 1)
    a4988.step(400, 1, 1)
    sleep(0.1)
print(time.ticks_us())