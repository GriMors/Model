from random import uniform
from vector import Vector
from cult import Cult
from demon import Demon
from berserk import Berserk

class World:

    def __init__(self, model):
        self.bodies = []
        self.model = model
        self.time = 0
        self.data_demons = []
        self.data_gr_demons = []
        self.data_cults = []
        self.step_time = 1

        self.count_berserk = []
        self.data_berserk = -1

    # добавление тела и спрайта
    def add_body(self, b):
        self.bodies.append(b)

    # удаление
    def remove(self, b):
        self.bodies.remove(b)

    # все действия в мире
    def act(self, dt):
        self.next_step(dt)
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
        for i in range(len(self.bodies)):
            b1 = self.bodies[i]
            if b1.deleted:
                continue
            v1 = b1.parent.view_body
            for j in range(i+1, len(self.bodies)):
                b2 = self.bodies[j]
                if b2.deleted:
                    continue
                v2 = b2.parent.view_body
                if b1.intersect(b2):
                    self.model.collision(b1.parent, b2.parent)
                elif b2.intersect(b1):
                    self.model.collision(b2.parent, b1.parent)
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

    def next_step(self, dt):
        if self.step_time >= 1:
            cults = [bd.parent for bd in self.bodies if type(bd.parent) == Cult]
            count_cult = sum([cult.settlers for cult in cults])
            demons = [bd.parent for bd in self.bodies if type(bd.parent) == Demon]
            count_demon = sum([demons.count for demons in demons])
            self.data_cults.append(len(cults))
            self.data_gr_demons.append(len(demons))
            self.data_demons.append(count_cult + count_demon)

            berserk = [bd.parent for bd in self.bodies if type(bd.parent) == Berserk]
            self.count_berserk.append(len(berserk))
            for i in range(len(self.count_berserk)):
                if self.count_berserk[i] != 0:
                    self.data_berserk = i+2
                    continue

            self.step_time = 0
            self.model.time_of_life += 1
        else:
            self.step_time += dt