from pico2d import *
import random
import main_state_2

xPos = [320, 1050, 910, 220, 400]
yPos = [250, 300, 200, 750, 680]

class Key :
    image = None
    def __init__(self) :
        if (Key.image == None) :
            self.image = load_image('KEY.png')
        self.x, self.y = xPos[main_state_2.KeyCount], yPos[main_state_2.KeyCount]
        self.collision = False
        self.Collision_sound = load_wav('PICKUP.wav')
        self.Collision_sound.set_volume(64)

    def draw(self) :
        if (self.collision == False) :
            self.image.draw(self.x, self.y)
            draw_rectangle(*self.get_bb())

    def update(self):
        pass

    def get_bb(self) :
        return self.x - 10, self.y - 10 , self.x + 10, self.y + 10

    def Collide(self) :
        self.Collision_sound.play()