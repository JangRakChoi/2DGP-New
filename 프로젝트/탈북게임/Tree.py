from pico2d import *
import random
import main_state

xPos = [210, 180, 700, 230, 590, 330, 650, 530, 100, 960, 1020, 640, 1200, 1200, 1200, 1200, 1200, 1200, 1200, 1200]
yPos = [323, 200, 900, 600, 430, 822, 540, 695, 120, 320, 700, 150, 900, 800, 600, 500, 400, 300, 200, 100]

class Tree :
    image = None
    def __init__(self) :
        if (Tree.image == None) :
            self.image = load_image('Tree.png')
        self.x, self.y = xPos[main_state.TreeCount], yPos[main_state.TreeCount]
        self.frame = random.randint(0, 1)
        main_state.TreeCount += 1

    def draw(self) :
            self.image.clip_draw(self.frame * 97, 0, 97, 154, self.x, self.y)

    def update(self):
        pass

    def get_bb(self) :
        return self.x - 20, self.y - 30 , self.x + 20, self.y - 10