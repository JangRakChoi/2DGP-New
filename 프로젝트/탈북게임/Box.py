from pico2d import *
import random
import main_state_2

xPos = [320, 1050, 910, 220, 400]
yPos = [250, 300, 200, 750, 680]

class Box :
    image = None
    def __init__(self) :
        if (Box.image == None) :
            self.image = load_image('box.png')
        self.Hp = 30
        self.x, self.y = xPos[main_state_2.BoxCount], yPos[main_state_2.BoxCount]
        main_state_2.BoxCount += 1

    def draw(self) :
        self.image.draw(self.x, self.y)

    def update(self):
        pass

    def get_bb(self) :
        return self.x - 50, self.y - 30 , self.x + 50, self.y + 30