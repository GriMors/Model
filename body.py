import const
import math
from vector import Vector

class Body:

    def __init__(self, pos, rad, v, parent):
        self.pos = pos
        self.rad = rad
        self.velocity = Vector(v[0], v[1])
        self.inter = []
        self.parent = parent
        self.type = type(parent)
        self.deleted = False
        self.see = False
        self.meet = False

    def set_velocity(self, v):
        self.velocity = Vector(v[0], v[1])

    def intersect(self, other):
        R = math.sqrt((self.pos[0]-other.pos[0])**2+(self.pos[1]-other.pos[1])**2)
        return R <= self.rad+other.rad

    def add_inter(self, body):
        self.inter.append(body)

    def move(self, dt):
        d = self.velocity.dx_dy()
        xy = (self.pos[0] + self.rad + d[0] * dt, self.pos[1] + self.rad + d[1] * dt)
        i = 0
        if (xy[0] > const.WINDOW) or (xy[0] < 0): d[0] *= -1; i = 1
        if (xy[1] > const.WINDOW) or (xy[1] < 0): d[1] *= -1; i = 1
        if i:
            l = self.velocity.lenght
            try:
                sign = d[1] / abs(d[1])
            except ZeroDivisionError:
                sign = 1
            try:
                a = sign * math.acos(d[0] / l) * 180 / math.pi
            except ZeroDivisionError:
                a = sign * math.acos(d[0] / 1) * 180 / math.pi
            self.velocity = Vector(l, a)
        self.pos[0] += d[0] * dt
        self.pos[1] += d[1] * dt