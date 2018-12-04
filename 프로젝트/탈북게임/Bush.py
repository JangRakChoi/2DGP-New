from pico2d import *
import random
import main_state

xPos = [400, 1100, 730]
yPos = [550, 680, 670]

class Bush :
    image = None
    def __init__(self) :
        if (Bush.image == None) :
            self.image = load_image('bush.png')
        self.x, self.y = xPos[main_state.BushCount], yPos[main_state.BushCount]
        self.frame = random.randint(0, 1)
        main_state.BushCount += 1

    def draw(self) :
        self.image.clip_draw(0, 0, 120, 120, self.x, self.y)

    def update(self):
        pass

    def get_bb(self) :
        return self.x - 30, self.y - 20 , self.x + 20, self.y + 30