from pico2d import *
import random
import main_state_3

xPos = [600, 1100, 1010, 980, 210, 180, 700, 230, 390, 330, 650, 530, 100, 960, 920, 640, 1200, 1200, 1200, 1200, 1200, 1200, 1200]
yPos = [100, 680, 900, 820, 323, 100, 900, 600, 410, 822, 540, 695, 120, 320, 780, 150, 800, 770, 620, 500, 300, 200, 100]

class Tree :
    image = None
    def __init__(self) :
        if (Tree.image == None) :
            self.image = load_image('Tree.png')
        self.x, self.y = xPos[main_state_3.TreeCount], yPos[main_state_3.TreeCount]
        self.frame = random.randint(0, 1)
        main_state_3.TreeCount += 1

    def draw(self) :
        self.image.clip_draw(self.frame * 97, 0, 97, 154, self.x, self.y)

    def update(self):
        pass

    def get_bb(self) :
        return self.x - 20, self.y - 70 , self.x + 20, self.y - 10