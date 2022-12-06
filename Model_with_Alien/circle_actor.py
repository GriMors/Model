import pygame

class CircleActor(pygame.sprite.Sprite):

    def __init__(self, body, color):
        pygame.sprite.Sprite.__init__(self)
        self.body = body
        self.color = color
        radius = self.body.rad

        self.image = pygame.Surface((2*radius, 2*radius), pygame.SRCALPHA)
        pygame.draw.circle(self.image, self.color, (radius, radius), radius)

    def update(self):
        self.rect = self.image.get_rect()
        self.rect.center = (self.body.pos[0], self.body.pos[1])