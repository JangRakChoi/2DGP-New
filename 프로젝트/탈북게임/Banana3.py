from pico2d import *
import random
import main_state_3

xPos = [320, 1090, 110, 880]
yPos = [250, 240, 900, 560]

class Banana :
    image = None
    def __init__(self) :
        if (Banana.image == None) :
            self.image = load_image('Banana.png')
        self.x, self.y = xPos[main_state_3.BananaCount], yPos[main_state_3.BananaCount]
        self.frame = random.randint(0, 1)
        main_state_3.BananaCount += 1
        self.Collision_sound = load_wav('PICKUP.wav')
        self.Collision_sound.set_volume(64)

    def draw(self) :
        self.image.draw(self.x, self.y)

    def update(self):
        pass

    def get_bb(self) :
        return self.x - 20, self.y - 20 , self.x + 20, self.y + 20

    def Collide(self) :
        self.Collision_sound.play()