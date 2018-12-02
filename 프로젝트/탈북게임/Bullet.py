from pico2d import *
import game_world


PIXEL_PER_METER = (10.0 / 0.3)
BULLET_SPEED_KMPH = 40.0
BULLET_SPEED_MPM = (BULLET_SPEED_KMPH * 1000.0 / 60.0)
BULLET_SPEED_MPS = (BULLET_SPEED_MPM / 60.0)
BULLET_SPEED_PPS = (BULLET_SPEED_KMPH * PIXEL_PER_METER)

# Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8

class Bullet:
    image = None

    def __init__(self, x=800, y=300, velocity=1):
        if Bullet.image == None:
            Bullet.image = load_image('Bullet.png')
        self.x, self.y, self.velocity = x, y, velocity

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        self.x += BULLET_SPEED_PPS

        if self.x < 25 or self.x > 1280 - 25:
            game_world.remove_object(self)