from body import Body
from circle_actor import CircleActor
import const

class Village:

    def __init__(self, pos, count, world):
        self.body = Body(pos, const.RADIUS_V, const.VELOCITY_V, self)
        self.circle = CircleActor(self.body, const.COLOR_V)
        self.view_body = Body(pos, const.RADIUS_V, const.VELOCITY_V, self)
        world.add_body(self.body)
        self.world = world
        self.ch_dt = 0
        self.settlers = count

    def __eq__(self, other):
        return (self.body.pos == other.body.pos,
                self.body.rad == other.body.rad,
                self.body.velocity.lenght == other.body.velocity.lenght,
                self.body.velocity.alpha == other.body.velocity.alpha)

    def population(self):
        self.settlers < const.MAX_POPULATION

    def update(self, dt):
        if self.population:
            self.ch_dt += dt
        if self.ch_dt > 5:
            self.settlers += 1
            self.ch_dt = 0