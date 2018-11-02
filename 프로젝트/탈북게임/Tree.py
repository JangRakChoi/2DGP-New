from pico2d import *
import random
import main_state

class Tree :
    image = None
    def __init__(self) :
        if (Tree.image == None) :
            self.image = load_image('Tree.png')
        self.x, self.y = main_state.x, main_state.y
        self.frame = random.randint(0, 2)
        main_state.x += random.randint(-10, 10) * 50
        main_state.y += random.randint(-10, 10) * 50
        main_state.x = clamp(50, main_state.x, 1280 - 50)
        main_state.y = clamp(50, main_state.y, 1000 - 50)

    def draw(self) :
            self.image.clip_draw(self.frame * 97, 0, 97, 154, self.x, self.y)

    def update(self):
        pass

    def get_bb(self) :
        return self.x - 20, self.y - 30 , self.x + 20, self.y - 10