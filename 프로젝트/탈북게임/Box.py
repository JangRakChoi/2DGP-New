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
        self.collision = False
        self.Attack_sound = load_wav('KICK.wav')
        self.Attack_sound.set_volume(64)

    def draw(self) :
        if (self.Hp > 0) :
            self.image.draw(self.x, self.y)
            draw_rectangle(*self.get_bb())

    def update(self):
        pass

    def get_bb(self) :
        if (self.Hp > 0) :
            return self.x - 50, self.y - 30 , self.x + 50, self.y + 30
        else :
            return -50, -50, -50, -50

    def Attack_box(self):
        self.Attack_sound.play()
        self.Hp -= 10
