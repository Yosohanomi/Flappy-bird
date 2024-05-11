import pygame
from random import randint

pygame.init()

win_width = 500
win_height = 500
FPS = 3

back = pygame.transform.scale(pygame.image.load('bird.jpg'), (win_width, win_height)) 

mw = pygame.display.set_mode((win_width, win_height))
mw.blit(back, (0, 0))

clock = pygame.time.Clock()

x=50
y=50

class Area():
    def __init__(self, x=0, y=0, width = 10, height = 10, color = None):
        self.rect = pygame.Rect(x, y, width, height)
        self.fill_color=  back
        if color:
            self.fill_color =  color
    def color(self, new_color):
        self.fill_color = new_color
    def fill(self):
        pygame.draw.rect(mw, self.fill_color, self.rect)
    def collidepoint(self, x, y):
        return self.rect.collidepoint(x, y)
    def colliderect(self, rect):
        return self.rect.collidepoint(rect)

class Picture(Area):
    def __init__(self, filename, x=0, y=0, width = 10, height = 10):
        Area.__init__(self, x=x, y=y, width=width, height=height, color=None)
        self.image = pygame.image.load(filename)
    def draw(self):
        mw.blit(self.image, (self.rect.x, self.rect.y))

class Label(Area):
    def set_text(self, text, fsize=12, text_color=(0,0,0)):
        self.image = pygame.font.SysFont("verdana" , fsize).render(text, True, text_color)
    def draw(self, shift_x, shift_y):
        self.fill()
        mw.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))

doge = Picture("doge.png", 160, 160, 50, 50)

game_over = False

while not game_over:
    doge.fill()
    doge.draw()
    pygame.display.update()
    clock.tick(60)