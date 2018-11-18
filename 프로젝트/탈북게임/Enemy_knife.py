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

class Enemy_Knife :
    def __init__(self) :
        self.image = load_image("enemy1.png")
        # soldier pivot : 50X50
        self.count = random.randint(0, 6)
        self.x, self.y = random.randint(20, 100) * 10, random.randint(5, 90) * 10
        self.cur_time = 0
        self.n = 0
        self.stop = random.randint(8, 15)
        self.where_collide = -1
        self.dir = random.random()*2*math.pi # random moving direction
        self.speed = 0
        self.timer = 1.0 # change direction every 1 sec when wandering
        self.frame = 0
        self.build_behavior_tree()  

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


