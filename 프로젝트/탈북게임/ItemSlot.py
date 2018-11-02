from pico2d import *


class ItemSlot :
    def __init__(self) :
        self.image = load_image('ItemSlot.png')

    def draw(self) :
        self.image.draw(200, 30)

    def update(self):
        pass