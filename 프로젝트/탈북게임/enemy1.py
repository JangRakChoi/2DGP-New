import game_framework
from pico2d import *
from BehaviorTree import BehaviorTree, SelectorNode, SequenceNode, LeafNode

import game_world
import random
import math
import main_state

PIXEL_PER_METER = (10.0 / 0.3)
RUN_SPEED_KMPH = 15.0
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

xPos = [600, 400, 500, 700, 900, 1000, 800]
yPos = [600, 400, 200, 400, 300, 500, 400]

class IdleState:
    @staticmethod
    def enter(boy, event):
        boy.frame = 0

    @staticmethod
    def exit(boy, event):
        pass

    @staticmethod
    def do(boy):
        boy.frame = (boy.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 6
        boy.timer += get_time() - boy.cur_time
        boy.cur_time = get_time()
        if boy.timer >= 3 :
           boy.cur_state = WalkState
           boy.timer = 0

    @staticmethod
    def draw(boy):
        if (boy.nowX > boy.x) :
            boy.image.clip_draw(int(boy.frame) * 77, 300, 78, 98, boy.x, boy.y)
        elif (boy.nowX <= boy.x):
            boy.image.clip_draw(int(boy.frame) * 77, 200, 78, 98, boy.x, boy.y)

class WalkState:
    @staticmethod
    def enter(boy, event):
        boy.frame = 0

    @staticmethod
    def exit(boy, event):
        pass

    @staticmethod
    def do(boy):
        boy.frame = (boy.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 6
        boy.x += boy.velocityRL * game_framework.frame_time
        boy.y += boy.velocityUD * game_framework.frame_time

        boy.n = boy.n + 1

        if (boy.n > 200):
            boy.n = 0
        t = boy.n / 200
        boy.nowX, boy.nowY = boy.x, boy.y
        boy.x = ((-t ** 3 + 2 * t ** 2 - t) * xPos[(boy.count - 3)] + (3 * t ** 3 - 5 * t ** 2 + 2) * xPos[(boy.count - 2)] + (-3 * t ** 3 + 4 * t ** 2 + t) * xPos[(boy.count - 1)] + (t ** 3 - t ** 2) * xPos[(boy.count)]) / 2
        boy.y = ((-t ** 3 + 2 * t ** 2 - t) * yPos[(boy.count - 3)] + (3 * t ** 3 - 5 * t ** 2 + 2) * yPos[(boy.count - 2)] + (-3 * t ** 3 + 4 * t ** 2 + t) * yPos[(boy.count - 1)] + (t ** 3 - t ** 2) * yPos[(boy.count)]) / 2
        if (boy.n == 200):
            boy.count = (boy.count + 1) % 7
        boy.x = clamp(50, boy.x, 1280 - 50)
        boy.y = clamp(50, boy.y, 1024 - 50)

        boy.x = clamp(25, boy.x, 1280 - 25)
        boy.y = clamp(25, boy.y, 1000 - 25)

        boy.timer += get_time() - boy.cur_time
        boy.cur_time = get_time()
        if boy.timer >= boy.stop:
            boy.timer = 0
            boy.stop = random.randint(8, 12)
            boy.cur_state = IdleState

    @staticmethod
    def draw(boy):
        if (boy.nowX > boy.x) :
            boy.image.clip_draw(int(boy.frame) * 78, 98, 78, 98, boy.x, boy.y)
        elif (boy.nowX <= boy.x):
            boy.image.clip_draw(int(boy.frame) * 78, 0, 78, 98, boy.x, boy.y)


class Enemy1 :
    def __init__(self) :
        self.image = load_image("enemy1.png")
        # soldier pivot : 50X50
        self.count = random.randint(0, 6)
        self.x, self.y = random.randint(20, 100) * 10, random.randint(5, 90) * 10
        self.frame = 0
        self.nowX, self.nowY, self.n = 0, 0, 0
        self.velocityRL, self.velocityUD = 0, 0
        self.event_que = []
        self.cur_state = WalkState
        self.cur_state.enter(self, None)
        self.cur_time = 0
        self.timer = 0
        self.n = 0
        self.stop = random.randint(8, 15)
        self.where_collide = -1

    def update(self) :
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state.enter(self, event)

    def draw(self) :
        self.cur_state.draw(self)
        draw_rectangle(*self.get_bb())

    def get_bb(self) :
        return self.x - 30, self.y - 50, self.x + 30, self.y + 50

    def add_event(self, event):
        self.event_que.insert(0, event)


