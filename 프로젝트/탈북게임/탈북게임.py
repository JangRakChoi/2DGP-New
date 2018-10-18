from pico2d import *
import random

open_canvas(1920, 1080)

class Map :
    def __init__(self) :
        self.image = load_image('map3.png')
    def draw(self) :
        self.image.draw(960, 540)

class Enemy:
    def __init__(self) :
        self.image = load_image("enemy.png")
        # soldier pivot : 50X50
        self.x, self.y = random.randint(500, 1800), random.randint(100, 1000)
        self.frame = 0

    def update(self) :
        pass

    def draw(self) :
        self.image.clip_draw(self.frame * 0, 200, 110, 100, self.x, self.y)

class Player:
    def __init__(self) :
        self.image = load_image("player.png")
        # soldier pivot : 50X50
        self.x, self.y = 300, 300
        self.frame = 0

    def draw(self) :
        self.image.clip_draw(self.frame, 80, 100, 80, self.x, self.y)

running = True

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


def update():
    pass

player = Player()
enemies = [Enemy() for n in range(4)]
background = Map()
MoveCheck = 0

while running:
    handle_events()
    for enemy in enemies:
        enemy.update()
    clear_canvas()
    background.draw()
    player.draw()
    for enemy in enemies :
        enemy.draw()
    update_canvas()
    delay(0.05)
    MoveCheck += 1

close_canvas()