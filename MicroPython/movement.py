from stepper import Stepper
from _thread import start_new_thread

tmc2209 = Stepper(18, 19)
a4988 = Stepper(17, 16)

def moveA(steps, time):
    if steps > 0:
        tmc2209.step(steps*8, 1, time)
    elif steps < 0:
        tmc2209.step(-steps*8, 0, time)
    
def moveB(steps, time):
    if steps > 0:
        a4988.step(steps*2, 0, time)
    elif steps < 0:
        a4988.step(-steps*2, 1, time)

class CoreXY:
    def __init__(self, x, y):
        self.x = x
        self.y = y
 
    def g0(self, x, y):
        stpA = (x - self.x) + (y - self.y)
        stpB = (x - self.x) - (y - self.y)
        time = (abs(stpA) + abs(stpB))/(10000/8)
        
        print(stpA)
        print(stpB)
        
        start_new_thread(moveB, (stpB, time))
        moveA(stpA, time)
            
        self.x = x
        self.y = y