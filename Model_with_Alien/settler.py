from body import Body
from circle_actor import CircleActor
import const

class Settler:

    def __init__(self, pos, v, world):
        self.body = Body(pos, const.RADIUS_S, v, self)
        self.circle = CircleActor(self.body, const.COLOR_S)
        self.view_body = Body(pos, const.RADIUS_S*10, v, self)
        world.add_body(self.body)
        self.world = world

    def __eq__(self, other):
        return (self.body.pos == other.body.pos,
                self.body.rad == other.body.rad,
                self.body.velocity.lenght == other.body.velocity.lenght,
                self.body.velocity.alpha == other.body.velocity.alpha)