from pico2d import *
import random
import main_state_2

xPos = [300, 1100]
yPos = [150, 700]

class Banana :
    image = None
    def __init__(self) :
        if (Banana.image == None) :
            self.image = load_image('Banana.png')
        self.x, self.y = xPos[main_state_2.BananaCount], yPos[main_state_2.BananaCount]
        self.frame = random.randint(0, 1)
        main_state_2.BananaCount += 1

    def draw(self) :
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())

    def update(self):
        pass

    def get_bb(self) :
        return self.x - 20, self.y - 20 , self.x + 20, self.y + 20