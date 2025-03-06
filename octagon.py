
# corner - угол, side - сторона,const - k 
#circum - описанная, inscr - вписанная
# oct - 8-угольник
from math import pi
from math import sqrt

class Octagon:
    # const
    corner = 135
    k = 1 + sqrt(2)
    
    #
    def __init__(self,side):
        self.side = side
        
    #
    def circum_r (self):
        r = (self.side/2)*sqrt(2+sqrt(2))

    #
    def circum_s (self):
        s = pi*((self.side/2)*sqrt(2+sqrt(2)))**2

    #
    def inscr_r (self):
        r = (self.side/2)*sqrt(2)

    #
    def inscr_s (self):
        s = pi*((self.side/2)*sqrt(2))**2

    #
    def oct_s (self):
        s = 2*2(1+sqrt(2))*self.side**2
    
    #
    def oct_p (self):
        p = 8*self.side


    
    def __del__(self):
        print("del done")


