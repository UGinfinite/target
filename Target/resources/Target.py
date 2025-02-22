import pygame

class Target:
    sprite = pygame.image.load('Sprites/targetSprite.png')

    def __init__(self, x = 0, y = 0, moving = False, distance = 0):
        self.Sx = x
        self.x = x
        self.y = y
        self.dir = 1
        self.dis = distance
        self.moving = moving
    def draw(self, surface):
        pygame.draw.rect(surface, 'black', (self.x, self.y, 80, 80))
        surface.blit(self.sprite, (self.x, self.y))
    def move(self, dt):
        if self.moving == True:
            self.x += 150 * self.dir * dt

            if self.x > self.Sx + self.dis * 3:
                self.dir *= -1

            if self.x < self.Sx:
                self.dir *= -1
