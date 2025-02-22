import pygame

class Box:
    box = pygame.image.load('Sprites/BoxSprite.png')
    
    def __init__(self, x = 0, y = 0, moving = False, dis = 0):
        self.Sx = x
        self.x = x
        self.y = y
        self.moving = moving
        self.dir = 1
        self.dis = dis
        
    def draw(self, surface):
        pygame.draw.rect(surface, 'black', (self.x, self.y, 62, 62))
        surface.blit(self.box, (self.x - 28, self.y - 28))
        
    def move(self, dt):
        if self.moving == True:
            self.x += 150 * self.dir * dt
            
            if self.x > self.Sx + self.dis * 3:
                self.dir *= -1
                
            if self.x < self.Sx:
                self.dir *= -1
