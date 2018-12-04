from pico2d import *
import random
import main_state

xPos = [100, 730]
yPos = [500, 670]

class Banana :
    image = None
    def __init__(self) :
        if (Banana.image == None) :
            self.image = load_image('Banana.png')
        self.x, self.y = xPos[main_state.BananaCount], yPos[main_state.BananaCount]
        self.frame = random.randint(0, 1)
        main_state.BananaCount += 1

    def draw(self) :
        self.image.draw(self.x, self.y)

    def update(self):
        pass

    def get_bb(self) :
        return self.x - 20, self.y - 20 , self.x + 20, self.y + 20