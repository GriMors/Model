import math

class Vector:
    def __init__(self, l, a):
        self.lenght = l
        self.alpha = (a/180)*math.pi

    def dx_dy(self):
        dx = self.lenght*math.cos(self.alpha)
        dy = self.lenght*math.sin(self.alpha)
        return ([dx, dy])