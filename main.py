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

# Primary condition 1:
for i in range(20):
    c = Cult([uniform(20, 685), uniform(20, 685)], int(uniform(1, 30)), world)
for i in range(1):
    berserk = Berserk([uniform(30, 670), uniform(30, 670)], (200, uniform(0, 360)), world)

# d2 = Demon([100, 320], const.RADIUS_D+10**(1/3), (50, 0), 33, world)
# d3 = Demon([300, 300], const.RADIUS_D+const.COUNT_D**(1/3), (50, 180), const.COUNT_D, world)

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

