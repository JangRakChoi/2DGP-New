import game_framework
from pico2d import *

import game_world
import random
import math

PIXEL_PER_METER = (10.0 / 0.3)
RUN_SPEED_KMPH = 20.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_KMPH * PIXEL_PER_METER)

WALK_SPEED_KMPH = 5.0
WALK_SPEED_MPM = (WALK_SPEED_KMPH * 1000.0 / 60.0)
WALK_SPEED_MPS = (WALK_SPEED_MPM / 60.0)
WALK_SPEED_PPS = (WALK_SPEED_KMPH * PIXEL_PER_METER)

# Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8

xPos = [random.randint(900, 1280 - 100) for n1 in range(20)]
yPos = [random.randint(0, 1024 - 100) for n2 in range(20)]


class Enemy :
    def __init__(self) :
        self.image = load_image("enemy.png")
        # soldier pivot : 50X50
        self.where = random.randint(0, 3)
        self.x, self.y = random.randint(900, 1280 - 200), random.randint(0, 1024 - 200)
        self.nowX, self.nowY = 0, 0
        self.frame = random.randint(0, 5)
        self.n = 0
        self.count = random.randint(0, 19)

    def update(self) :
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 6
        self.n = self.n + 1
        if (self.n > 200) :
            self.n = 0
        t = self.n / 200
        self.nowX, self.nowY = self.x, self.y
        self.x = ((-t ** 3 + 2 * t ** 2 - t) * xPos[(self.count - 3)] + (3 * t ** 3 - 5 * t ** 2 + 2) * xPos[(self.count - 2)] + (
                    -3 * t ** 3 + 4 * t ** 2 + t) * xPos[(self.count - 1)] + (t ** 3 - t ** 2) * xPos[(self.count)]) / 2
        self.y = ((-t ** 3 + 2 * t ** 2 - t) * yPos[(self.count - 3)] + (3 * t ** 3 - 5 * t ** 2 + 2) * yPos[(self.count - 2)] + (
                    -3 * t ** 3 + 4 * t ** 2 + t) * yPos[(self.count - 1)] + (t ** 3 - t ** 2) * yPos[(self.count)]) / 2
        if (self.n == 200) :
            self.count = (self.count + 1) % 20
        self.x = clamp(50, self.x, 1280 - 50)
        self.y = clamp(50, self.y, 1024 - 50)

    def draw(self) :
        if (self.nowX > self.x) :
            self.image.clip_draw(int(self.frame) * 103, 100, 103, 103, self.x, self.y)
        elif (self.nowX <= self.x):
            self.image.clip_draw(int(self.frame) * 103, 0, 103, 103, self.x, self.y)

    def get_bb(self) :
        return self.x - 50, self.y - 50, self.x + 50, self.y + 50
