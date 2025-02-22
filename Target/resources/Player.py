import pygame, time

class Player:
    sprite = pygame.image.load('Sprites/PlayerSprite.png')

    def __init__(self, x = 360, y = 600 - (50 + 15)):
        self.x = x
        self.y = y
    def move(self, dir, dt):
        self.x += 400 * dir * dt
    def draw(self, surface):
        surface.blit(self.sprite, (self.x - 10, self.y))
