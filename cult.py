import const
from body import Body

class Cult:

    def __init__(self, pos, demons, world):
        self.body = Body(pos, const.RADIUS_C, const.VELOCITY_C, self)
        self.view_body = Body(pos, 0, const.VELOCITY_C, self)
        world.add_body(self.body)
        self.settlers = demons
        self.world = world
        self.ch_dt = 0

    def __eq__(self, other):
        return (self.body.pos == other.body.pos,
                self.body.rad == other.body.rad,
                self.body.velocity.lenght == other.body.velocity.lenght,
                self.body.velocity.alpha == other.body.velocity.alpha)

    def population(self):
        return self.settlers < const.MAX_POPULATION

    def update(self, dt):
        if self.population:
            self.ch_dt += dt
        if self.ch_dt > 5:
            self.settlers += 1
            self.ch_dt = 0
