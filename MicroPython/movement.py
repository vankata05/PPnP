from stepper import Stepper

tmc2209 = Stepper(18, 19)
a4988 = Stepper(17, 16)

def moveA(steps, dir_):
    tmc2209.step(steps*8, dir_, 1)
    
def moveB(steps, dir_):
    a4988.step(steps, dir_, 1)

class CoreXY:
    def __init__(self, x, y):
        self.x = x
        self.y = y
 
    def G0(self, x, y):
        stpA = (x - self.x) + (y - self.y)
        stpB = (x - self.x) - (y - self.y)
        
        print(stpA)
        print(stpB)
        
        if stpA > 0:
            moveA(stpA, 1)
        elif stpA < 0:
            moveA(stpA*-1, 0)
        
        if stpB > 0:
            moveB(stpB, 1)
        elif stpB< 0:
            moveB(stpB*-1, 0)
            
        self.x = x
        self.y = y