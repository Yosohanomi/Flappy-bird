import pygame
from random import randint
import time

pygame.init()

clock = pygame.time.Clock()
back = (0,206,209)

mw = pygame.display.set_mode((500,500))
mw.fill(back)
class Area():
    def __init__(self, x=0,y=0, width=10, height=10, color=None ):
        self.rect = pygame.Rect(x,y,width,height)
        self.fill_color = color
    def color(self,new_color):
        self.fill_color = new_color
    def fill(self):
        pygame.draw.rect(mw, self.fill_color, self.rect)
    def outline(self, frame_color, thickness):
        pygame.draw.rect(mw, frame_color, self.rect, thickness)
    def collidepoint(self, x, y):
        return self.rect.collidepoint(x,y)
class Label(Area):
    def set_text(self, text, fsize=12, text_color=(0,0,0)):
        self.image = pygame.font.SysFont("verdana" , fsize).render(text, True, text_color)
    def draw(self, shift_x, shift_y):
        self.fill()
        mw.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))
yellow = (255, 255, 0)
blue = (80,80,255)
green = (0,255,0)
red = (255,0,0)

cards = []
num_cards = 4

x = 70
for i in range(num_cards):
    new_card = Label(x, 170, 70, 100, yellow)
    new_card.outline(blue, 10)
    new_card.set_text("Click", 26)
    cards.append(new_card)
    x += 100
score_text = Label(330, 0 ,50, 50, back)
score_text.set_text("Рахунок:", 45, yellow)
score_text.draw(20,20)

score = Label(430, 55 ,50, 40, back)
score.set_text("0", 40, yellow)
score.draw(0,0)

start_time = time.time()
cur_time = start_time

time_text = Label(0, 0 ,50, 50, back)
time_text.set_text("Час:", 40, yellow)
time_text.draw(20,20)

timer = Label(50, 55 ,50, 40, back)
timer.set_text("0", 40, yellow)
timer.draw(0,0)
wait = 0
points = 0
while True:
    if wait == 0:
        wait = 20
        click = randint(1, num_cards)
        for i in range(num_cards):
            cards[i].color(yellow)
            if(i+1)==click:
                cards[i].draw(10,40)
            else:
                cards[i].fill()
    else:
        wait -= 1
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x, y = event.pos
            for i in range(num_cards):
                if cards[i].collidepoint(x,y):
                    if i+1 == click:
                        cards[i].color(green)
                        points +=1
                    else:
                        cards[i].color(red)
                        points -=1
                    cards[i].fill()
                    score.set_text(str(points), 40, yellow)
                    score.draw(0,0)

    new_time = time.time()

    if new_time - start_time >= 11:
        win = Label(0, 0, 500, 500, yellow)
        win.set_text("Час вичерпано!", 60, blue)
        win.draw(100, 180)
        break
    
    if int(new_time) - int(cur_time) == 1:
        timer.set_text(str(int(new_time-start_time)), 40, yellow)
        timer.draw(0, 0)
        cur_time = new_time


    if points >=5:
        win = Label(0, 0, 500, 500, yellow)
        win.set_text("Ти переміг!", 60, blue)
        win.draw(140, 180)
        result_time = Label(90, 230, 250, 250, yellow)
        result_time.set_text("Час проходження: " + str(int(new_time - start_time)) + "секунд", 40, blue)
        result_time.draw(0, 0)
        break

    pygame.display.update()
    clock.tick(40)
pygame.display.update()