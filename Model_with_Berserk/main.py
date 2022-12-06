import pygame
# установка посредством команды "pip install pygame"
import const
import time
from model import Model
from cult import Cult
from berserk import Berserk

# инициировали pygame
pygame.init()
# создали экран заданного размера
screen = pygame.display.set_mode((const.WINDOW, const.WINDOW))
pygame.display.set_caption("Test circles")
# получили объект отвечающий за время
clock = pygame.time.Clock()
# инициировали спрайты (рисуемые объекты)
all_sprites = pygame.sprite.Group()

model = Model()
world = model.world

c1 = Cult([100, 100], 20, world)
c2 = Cult([500, 500], 5, world)
berserk = Berserk([300, 300], (300, 30), world)
all_sprites.add(c1.circle)
all_sprites.add(c2.circle)
all_sprites.add(berserk.circle)

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
    all_sprites.update()
    t1 = t2
    # отрисовка
    screen.fill(const.WHITE)
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()

