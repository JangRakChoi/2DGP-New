from pico2d import *
import random
import main_state_3

xPos = [400, 1100, 730, 770, 250, 625]
yPos = [150, 390, 700, 420, 480, 270]

class Bush :
    image = None
    def __init__(self) :
        if (Bush.image == None) :
            self.image = load_image('bush.png')
        self.x, self.y = xPos[main_state_3.BushCount], yPos[main_state_3.BushCount]
        self.frame = random.randint(0, 1)
        main_state_3.BushCount += 1

    def draw(self) :
        self.image.clip_draw(0, 0, 120, 120, self.x, self.y)

    def update(self):
        pass

    def get_bb(self) :
        return self.x - 30, self.y - 30 , self.x + 30, self.y + 30