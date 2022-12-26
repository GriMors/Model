import pygame
import math
import const
from random import uniform
from cult import Cult
from berserk import Berserk
from demon import Demon
from world import World
from vector import Vector

class Model:

    def __init__(self):
        self.world = World(self)
        self.time = 0
        self.time_of_life = 0

    # взаимодействия в мире
    def collision(self, object1, object2):
        if type(object1) == Cult:
            if type(object2) == Berserk:
                self.fight(object1, object2)
            elif type(object2) == Demon:
                if object2.body.meet == False:
                    object2.body.meet = True
                    self.join_in_cult(object1, object2)
        if type(object1) == Demon:
            if type(object2) == Demon:
                if self.world.time > self.time + 0.5:
                        self.create_group(object1, object2)

    # вступление демонов в культ
    def join_in_cult(self, object1, object2):
        if object1.population():
            count_in_cult = const.MAX_POPULATION - object1.settlers
            if count_in_cult < object2.count:
                object1.settlers += count_in_cult
                self.separation_group(object2, count_in_cult)
            else:
                object1.settlers += object2.count
                object2.body.deleted = True
        object2.body.meet = False

    # создание групп демонов
    def create_group(self, object1, object2):
        pos = object1.body.pos
        v = [const.VELOCITY_D, uniform(0, 360)]
        count1 = object1.count
        count2 = object2.count
        sum = count1 + count2
        if sum >= const.MAX_POPULATION:
            count_demon = sum - const.MAX_POPULATION
            Cult([pos[0], pos[1]], const.MAX_POPULATION, self.world)
            if count_demon > 0:
                Demon([pos[0], pos[1]], const.RADIUS_D + count_demon ** (1/3), v, count_demon, self.world)
        else:
            Demon([pos[0], pos[1]], const.RADIUS_D + sum ** (1/3), v, sum, self.world)
        object1.body.deleted = True
        object2.body.deleted = True

    # разделение групп демонов
    def separation_group(self, object, count_in_cult):
        pos = object.body.pos
        v = [const.VELOCITY_D, uniform(0, 360)]
        count = object.count
        new_count = count - count_in_cult
        Demon([pos[0], pos[1]], const.RADIUS_D + new_count ** (1/3), v, new_count, self.world)
        object.body.deleted = True

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
                Demon([pos[0], pos[1]], const.RADIUS_D + const.COUNT_D ** (1/3), [const.VELOCITY_D, uniform(20, 685)], const.COUNT_D, self.world)
        object1.body.deleted = True

    # обзор тел
    def detection(self, object1, object2):
        if type(object1) == Berserk:
            if type(object2) == Cult:
                self.detection_BorDandC(object1, object2)
        elif type(object1) == Demon:
            if type(object2) == Cult:
                self.detection_BorDandC(object1, object2)
            elif type(object2) == Demon:
                self.detection_BorDandC(object1, object2)

    # "заметил - повернул"
    def detection_BorDandC(self, object1, object2):
        if object1.body.see == False:
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
        try:
            a = sign * math.acos(dx / l) * 180 / math.pi
        except ZeroDivisionError:
            a = sign * math.acos(dx / 1) * 180 / math.pi
        l = bd_1.velocity.lenght
        bd_1.velocity = Vector(l, a)

    # увеличение числа демонов со временем
    def life(self, object, dt):
        if type(object) == Cult:
            if object.population():
                object.update(dt)