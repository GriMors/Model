import pygame
import math
import const
from random import uniform
from cult import Cult
from berserk import Berserk
from demon import Demon
from world import World
from vector import Vector
all_sprites = pygame.sprite.Group()


class Model:

    def __init__(self):
        self.world = World(self, all_sprites)
        self.time = 0

    # взаимодействия в мире
    def collision(self, object1, object2):
        if type(object1) == Cult:
            if type(object2) == Berserk:
                self.fight(object1, object2)
            elif type(object2) == Demon:
                if object2.body.meet != True:
                    object2.body.meet = True
                    self.join_in_cult(object1, object2)
        if type(object1) == Demon:
            if type(object2) == Demon:
                if self.world.time > self.time + 1:
                    if object1.body.meet != True:
                        object1.body.meet = True
                        if object2.body.meet != True:
                            object2.body.meet = True
                            self.create_group(object1, object2)

    # вступление демонов в культ
    def join_in_cult(self, object1, object2):
        if object1.population():
            count_in_cult = const.MAX_POPULATION - object1.settlers
            # print('object1.settlers-1', object1.settlers)
            if count_in_cult < object2.count:
                object1.settlers += count_in_cult
                # print('object1.settlers-2', object1.settlers)
                self.seraration_group(object2, count_in_cult)
            else:
                object1.settlers += object2.count
                object2.body.deleted = True
                object2.circle.kill()

    # создание групп демонов
    def create_group(self, object1, object2):
        pos = object1.body.pos
        v = [200, uniform(0, 360)]
        # v = [100, 0]
        rad = object1.body.rad
        count1 = object1.count
        count2 = object2.count
        Demon([pos[0], pos[1]], rad + 0.5 * const.RADIUS_D * count2, v, count1 + count2, self.world)
        object1.body.deleted = True
        object1.circle.kill()
        object2.body.deleted = True
        object2.circle.kill()

    # разделение групп демонов
    def seraration_group(self, object, count_in_cult):
        pos = object.body.pos
        v = [200, uniform(0, 360)]
        # v = [100, 0]
        rad = object.body.rad
        count = object.count
        Demon([pos[0], pos[1]], rad - const.RADIUS_D*count_in_cult*0.5, v, count - count_in_cult, self.world)
        object.body.deleted = True
        object.circle.kill()

    # сражение Берсерка с культом
    def fight(self, object1, object2):
        if object1.settlers > object2.power:
            self.death_B(object1, object2)
        else:
            self.death_C(object1)
            self.time = self.world.time
            return self.time

    # гибель Берсерка
    def death_B(self, object1, object2):
            object2.body.deleted = True
            object2.circle.kill()
            n = object1.settlers
            object1.settlers -= int(2 * const.POWER - n)

    # уничтожение культа - создание демонов
    def death_C(self, object1):
        n = object1.settlers
        object1.settlers = int(n - 0.5 * const.POWER)
        object1.child = 0
        if object1.settlers > 0:
            pos = object1.body.pos
            for i in range(object1.settlers):
                Demon([pos[0], pos[1]], const.RADIUS_D, [200, uniform(20, 685)], 1, self.world)
        object1.body.deleted = True
        object1.circle.kill()

    # обзор тел
    def detection(self, object1, object2):
        if type(object1) == Berserk:
            if type(object2) == Cult:
                self.detection_BorDandC(object1, object2)
        elif type(object1) == Demon:
            if type(object2) == Cult:
                self.detection_BorDandC(object1, object2)
        # elif type(object1) == Demon:
        #     if type(object2) == Demon:
        #         # self.detection_BorDandC(object1, object2)
        #         if object1.body.see != True:
        #             object1.body.see = True
        #             self.turn(object1.body, object2.body)

    # "заметил - повернул"
    def detection_BorDandC(self, object1, object2):
        if object1.body.see != True:
            object1.body.see = True
            self.turn(object1.body, object2.body)

    # поворот к цели
    def turn(self, bd_1, bd_2):
        dx = bd_2.pos[0] - bd_1.pos[0]
        dy = bd_2.pos[1] - bd_1.pos[1]
        l = math.sqrt(dx**2 + dy**2)
        try:
            sign = dy / abs(dy)
        except ZeroDivisionError:
            sign = 1
        a = sign * math.acos(dx / l) * 180 / math.pi
        l = bd_1.velocity.lenght
        bd_1.velocity = Vector(l, a)

    # увеличение числа демонов со временем
    def life(self, object, dt):
        if type(object) == Cult:
            if object.population():
                object.update(dt)
                # print('demons: ', object.settlers)