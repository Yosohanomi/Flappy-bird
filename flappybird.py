import pygame
from random import randint
from time import sleep

pygame.init()

win_width = 500
win_height = 500
FPS = 3

# back = pygame.transform.scale(pygame.image.load('bird.jpg'), (win_width, win_height)) 

mw = pygame.display.set_mode((win_width, win_height))
# mw.blit(back, (0, 0))

clock = pygame.time.Clock()

x=50
y=50

class Area():
    def __init__(self, x=0, y=0, width = 10, height = 10, color = None):
        self.rect = pygame.Rect(x, y, width, height)
        # self.rect = pygame.Surface((width, height))
        self.fill_color = (61, 176, 205)
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



dog_x = 160
dog_y = 160
# dog = Picture("siba-removebg-preview.png", 160, 160, 70, 70)

move_up = False
move_down = False

game_over = False
i = 0

while not game_over:
    # dog.fill()
    back = pygame.transform.scale(pygame.image.load('bird.jpg'), (win_width, win_height))
    mw.blit(back, (0, 0))
    dog = pygame.image.load("siba-removebg-preview.png")
    mw.blit(dog, (dog_x, dog_y))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                move_up = True
            if event.key == pygame.K_DOWN:
                move_down = True
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                move_up = False
            if event.key == pygame.K_DOWN:
                move_down = False

        if move_up:
            while i != 10:
                sleep(0.001)
                dog_y -= 1
                mw.blit(dog, (dog_x, dog_y))
                # dog.rect.y +=3
                i +=1

        if move_down:
            while i != 10:
                sleep(0.001)
                dog_y += 1
                mw.blit(dog, (dog_x, dog_y))
                # dog.rect.y -= 3
                i +=1
        i = 0
    dog_y -= -0.3
    # dog.draw()
    # pygame.display.update()
    pygame.display.flip()
    clock.tick(60)
    