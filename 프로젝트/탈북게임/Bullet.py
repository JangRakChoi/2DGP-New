from pico2d import *
import game_world
import game_framework


PIXEL_PER_METER = (10.0 / 0.3)
BULLET_SPEED_KMPH = 10.0
BULLET_SPEED_MPM = (BULLET_SPEED_KMPH * 1000.0 / 60.0)
BULLET_SPEED_MPS = (BULLET_SPEED_MPM / 60.0)
BULLET_SPEED_PPS = (BULLET_SPEED_KMPH * PIXEL_PER_METER)

class Bullet:
    image = None

    def __init__(self, x, y, velocity):
        if Bullet.image == None:
            Bullet.image = load_image('Bullet.png')
        self.x, self.y, self.velocity = x, y, velocity
        self.speed = BULLET_SPEED_PPS

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        self.dir = math.atan2(self.dest_y - self.y, self.dest_x - self.x)
        self.x += self.speed * math.cos(self.dir) * game_framework.frame_time
        if self.x < 25 or self.x > 1280 - 25:
            game_world.remove_object(self)