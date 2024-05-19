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


class Bones():
    def __init__(self, x, y, bone_offset=230):
        self.bone = pygame.image.load("bone.png")
        self.x = x
        self.y = y
        self.offset = bone_offset

    def draw(self):
        mw.blit(self.bone, (self.x, self.y))
        mw.blit(self.bone, (self.x, self.y - self.offset))

    def move(self, move_x):
        self.x -= move_x


class Dog():
    def __init__(self, x, y):
        self.dog = pygame.image.load("siba-removebg-preview.png")
        self.x = x
        self.y = y

    def draw(self):
        mw.blit(self.dog, (self.x, self.y))

    def move(self, move_y):
        self.y += move_y

    def auto_fall(self, move_y=0.3):
        self.y += move_y

    def bone_was_hit(self, bones, bone_width=30, bone_height=40):
        top_bone_y_correction = 85
        for bone in bones:
            dog_in_x_area = (dog.x > bone.x - bone_width) and (dog.x < bone.x + bone_width)
            dog_in_y_bottom_area = (dog.y > bone.y - bone_height) and (dog.y < bone.y + bone_height)
            bone_y_coord = bone.y - bone.offset + top_bone_y_correction
            dog_in_y_top_area = (dog.y > bone_y_coord - bone_height) and (dog.y < bone_y_coord + bone_height)
            dog_in_y_area = dog_in_y_bottom_area or dog_in_y_top_area
            if dog_in_x_area and dog_in_y_area:
                return True
        
        return False


# def check_collision(dog, bones_list):
#     for bone in bones_list:
#         if dog.

black = (0, 0, 0)

dog_x = 160
dog_y = 160
# dog = Picture("siba-removebg-preview.png", 160, 160, 70, 70)

bone_x = 200
bone_y = 250

move_up = False
move_down = False

game_over = False
i = 0

sand = (228, 214, 167)

bones_list = []
dog = Dog(dog_x, dog_y)

points = 0

while not game_over:
    # dog.fill()
    back = pygame.transform.scale(pygame.image.load('bird.jpg'), (win_width, win_height))
    mw.blit(back, (0, 0))
    # dog = pygame.image.load("siba-removebg-preview.png")
    # mw.blit(dog, (dog_x, dog_y))

    # bone_top = pygame.image.load("bone.png")
    # mw.blit(bone_top, (bone_x, bone_y))

    # bone_bottom = pygame.image.load("bone.png")
    # mw.blit(bone_bottom, (bone_x, bone_y-230))

    score_text = Label(10, 410 ,50, 50, sand)
    score_text.set_text("Рахунок:", 30, black)
    score_text.draw(20,20)

    score = Label(200, 430 ,50, 40, sand)
    score.set_text("0", 30, black)
    score.draw(0,0)

    last_bone_x = bones_list[-1].x if bones_list else dog_x

    if bones_list and (bones_list[0].x + 85 < 0):
        del bones_list[0]

    while (last_bone_x + 70) < win_width:
        random_y_offset = randint(0, 2) * 10
        random_direction = (-1) ** randint(0, 1)
        bones_list.append(Bones(last_bone_x + 70, bone_y + random_y_offset * random_direction))
        last_bone_x += 70

    for bone_el in bones_list:
        bone_el.move(1)
        bone_el.draw()

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

        # if move_up:
        #     while i != 10:
        #         sleep(0.001)
        #         # dog_y -= 1
        #         dog.move(-1)
        #         dog.draw()
        #         # mw.blit(dog, (dog_x, dog_y))
        #         # dog.rect.y +=3
        #         i +=1

        if move_up:
            dog.move(-6)

        if move_down:
            dog.move(6)
        
        # if move_down:
        #     while i != 10:
        #         sleep(0.001)
        #         # dog_y += 1
        #         dog.move(1)
        #         dog.draw()
        #         # mw.blit(dog, (dog_x, dog_y))
        #         # dog.rect.y -= 3
        #         i +=1
        # i = 0

    if dog.bone_was_hit(bones_list):
            lose_text = Label(150, 150, 80, 40, None)
            lose_text.set_text("You lose! :(", 60, black)
            lose_text.draw(-80, 110)
            sleep(1)
            game_over = True

    dog.auto_fall()
    dog.draw()

    dog_y -= -0.3
    # bone_x -=0.3

    # dog.draw()
    # pygame.display.update()
    pygame.display.flip()
    clock.tick(60)
    