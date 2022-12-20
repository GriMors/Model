from random import uniform
from vector import Vector
from cult import Cult
from demon import Demon

class World:

    def __init__(self, model, all_sprites):
        self.bodies = []
        self.model = model
        self.all_sprites = all_sprites
        self.time = 0
        self.demons = []
        self.cults = []

    # добавление тела и спрайта
    def add_body(self, b):
        self.bodies.append(b)
        self.all_sprites.add(b.parent.circle)

    # удаление
    def remove(self, b):
        self.bodies.remove(b)

    # все действия в мире
    def act(self, dt):
        self.time_to_turn(dt)
        self.collisions()
        for b in self.bodies:
            if type(b.parent) == Cult:
                self.model.life(b.parent, dt)
            if b.deleted:
                self.remove(b)
            if not self.time and not b.see:
                b.velocity = Vector(b.velocity.lenght, uniform(0, 360))
            b.move(dt)
            b.parent.view_body.pos = b.pos

    # обработка пересечений тел (взаимодействий)
    def collisions(self):
        # l = len(self.bodies)
        # for i in range(l):
        for i in range(len(self.bodies)):
            b1 = self.bodies[i]
            if b1.deleted:
                continue
            v1 = b1.parent.view_body
            # for j in range(i+1, l):
            for j in range(i+1, len(self.bodies)):
                b2 = self.bodies[j]
                if b2.deleted:
                    continue
                v2 = b2.parent.view_body
                # if b1.intersect(b2) and not (b1 in b2.inter):
                #     b1.add_inter(b2)
                #     b2.add_inter(b1)
                if b1.intersect(b2):
                    self.model.collision(b1.parent, b2.parent)
                elif v1.intersect(b2):
                    self.model.detection(b1.parent, b2.parent)
                elif v2.intersect(b1):
                    self.model.detection(b2.parent, b1.parent)
                if b1.deleted:
                    b2.see = False
                elif b2.deleted:
                    b1.see = False

    # время для смены направления
    def time_to_turn(self, dt):
        if self.time >= 5:
            self.time = 0
            return True
        self.time += dt
        return False