from pico2d import *

class Map :
    def __init__(self) :
        self.image = load_image('map2.png')

    def draw(self) :
        self.image.draw(960, 540)

    def update(self):
        pass