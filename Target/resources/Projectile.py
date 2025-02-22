import pygame

class Projectile:
    def __init__(self, x, y):
        self.x = x + 17
        self.y = y + 15
        self.dir = 1
    def draw(self, surface):
        pygame.draw.rect(surface, 'black', (self.x + 3, self.y + 2, 8, 8))
        pygame.draw.circle(surface, 'dark gray', (self.x + 8, self.y + 7), 5)
    def move(self, dt):
        self.y -= 450 * self.dir * dt
    def setDir(self, dir):
        self.dir = dir
