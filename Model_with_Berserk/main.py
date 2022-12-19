import pygame
# установка посредством команды "pip install pygame"
import const
import time
from random import uniform
from model import Model
from cult import Cult
from berserk import Berserk
from demon import Demon


# инициировали pygame
pygame.init()
# создали экран заданного размера
screen = pygame.display.set_mode((const.WINDOW, const.WINDOW))
pygame.display.set_caption("Test circles")
# получили объект отвечающий за время
clock = pygame.time.Clock()

# Создание модели и соответствующего мира
model = Model()
world = model.world


# Primary condition:
# c1 = Cult([480, 450], 25, world)
# c2 = Cult([420, 450], 24, world)
# c1 = Cult([200, 500], 25, world)
c2 = Cult([500, 400], 24, world)
#
# c1 = Cult([uniform(20, 685), uniform(20, 685)], int(uniform(1, 30)), world)
# c2 = Cult([uniform(20, 685), uniform(20, 685)], int(uniform(1, 30)), world)
# c3 = Cult([uniform(20, 685), uniform(20, 685)], int(uniform(1, 30)), world)
# c4 = Cult([uniform(20, 685), uniform(20, 685)], int(uniform(1, 30)), world)
# c5 = Cult([uniform(20, 685), uniform(20, 685)], int(uniform(1, 30)), world)
# c6 = Cult([uniform(20, 685), uniform(20, 685)], int(uniform(1, 30)), world)
# c7 = Cult([uniform(20, 685), uniform(20, 685)], int(uniform(1, 30)), world)
# c8 = Cult([uniform(20, 685), uniform(20, 685)], int(uniform(1, 30)), world)
# c9 = Cult([uniform(20, 685), uniform(20, 685)], int(uniform(1, 30)), world)
# c10 = Cult([uniform(20, 685), uniform(20, 685)], int(uniform(1, 30)), world)
# c11 = Cult([600, 300], int(34), world)
#
# berserk = Berserk([100, 100], (200, uniform(0, 360)), world)
# berserk = Berserk([200, 200], (160, 35), world)
#
# d1 = Demon([460, 300], const.RADIUS_D, (40, 90), 1, world)
d2 = Demon([100, 300], const.RADIUS_D*1.5, (50, 0), 2, world)
d3 = Demon([300, 320], const.RADIUS_D, (50, 180), 1, world)


running = True
t1 = time.time()
while running:
    # держим частоту кадров не выше
    clock.tick(const.FPS)

    for event in pygame.event.get():
        # проверить закрытие окна
        if event.type == pygame.QUIT:
            running = False

    # обновление
    t2 = time.time()
    dt = (t2-t1)
    world.act(dt)
    world.all_sprites.update()
    t1 = t2
    # отрисовка
    screen.fill(const.WHITE)
    world.all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()

