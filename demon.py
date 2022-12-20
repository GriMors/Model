import const
from body import Body
from actor import Actor

class Demon:

    def __init__(self, pos, rad, v, count, world):
        self.body = Body(pos, rad, v, self)
        self.circle = Actor(self.body, const.COLOR_D)
        self.view_body = Body(pos, rad * const.FOR_VIEW_D, v, self)
        world.add_body(self.body)
        self.world = world
        self.count = count

    def __eq__(self, other):
        return (self.body.pos == other.body.pos,
                self.body.rad == other.body.rad,
                self.body.velocity.lenght == other.body.velocity.lenght,
                self.body.velocity.alpha == other.body.velocity.alpha,
                self.count == other.count)