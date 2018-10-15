from pico2d import *
import random

open_canvas()

class Map :
    def __init__(self) :
        self.image = load_image('map3.png')
    def draw(self) :
        self.image.draw(300, 300)

class Player:
    pass

class Enemy:
    pass

def handle_events():
    pass

def update():
    pass

player = Player()
background = Map()
running = True

while running:
    background.draw()
    update_canvas()
    delay(0.05)

close_canvas()