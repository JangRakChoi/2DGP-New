from pico2d import *
import random

open_canvas()

class Map :
    def __init__(self) :
        self.image = load_image('map3.png')
    def draw(self) :
        self.image.draw(300, 300)

class Enemy:
    def __init__(self) :
        self.image = load_image("soldier2.png")
        # soldier pivot : 50X50
        self.x, self.y = 100, 100
        self.frame = 0

    def draw(self) :
        self.image.draw(self.x, self.y, 100, 100)

class Player:
    def __init__(self) :
        self.image = load_image("animation_sheet.png")
        # soldier pivot : 50X50
        self.x, self.y = 300, 300
        self.frame = 0

    def draw(self) :
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)


def handle_events():
    pass

def update():
    pass

player = Player()
enemy = Enemy()
background = Map()
running = True

while running:
    clear_canvas()
    background.draw()
    player.draw()
    enemy.draw()
    update_canvas()
    delay(0.05)

close_canvas()