from pico2d import *
import random
import main_state_3

xPos = [320, 1110, 880, 110, 400, 570]
yPos = [250, 240, 560, 900, 680, 990]

class Key :
    image = None
    def __init__(self) :
        if (Key.image == None) :
            self.image = load_image('KEY.png')
        self.x, self.y = xPos[main_state_3.KeyCount], yPos[main_state_3.KeyCount]
        self.collision = False
        self.Collision_sound = load_wav('PICKUP.wav')
        self.Collision_sound.set_volume(64)

    def draw(self) :
        if (self.collision == False) :
            self.image.draw(self.x, self.y)

    def update(self):
        pass

    def get_bb(self) :
        return self.x - 10, self.y - 10 , self.x + 10, self.y + 10

    def Collide(self) :
        if self.collision == False :
            self.Collision_sound.play()