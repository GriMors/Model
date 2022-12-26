import const
from body import Body

class Berserk:

    def __init__(self, pos, v, world):
        self.body = Body(pos, const.RADIUS_B, v, self)
        self.view_body = Body(pos, const.RADIUS_VB, v, self)
        world.add_body(self.body)
        self.world = world
        self.power = const.POWER

    def __eq__(self, other):
        return (self.body.pos == other.body.pos,
                self.body.rad == other.body.rad,
                self.body.velocity.lenght == other.body.velocity.lenght,
                self.body.velocity.alpha == other.body.velocity.alpha)