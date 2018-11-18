import game_framework
from pico2d import *
from BehaviorTree import BehaviorTree, SelectorNode, SequenceNode, LeafNode

import game_world
import random
import math
import main_state

PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 10.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# zombie Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 10

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

    def wander(self):
        self.speed = RUN_SPEED_PPS
        self.timer -= game_framework.frame_time
        if self.timer < 0 :
            self.timer += 1.0
            self.dir = random.random()*2*math.pi

        return BehaviorTree.SUCCESS

    def find_player(self):
       player = main_state.get_player()
       distance = (player.x - self.x) ** 2 + (player.y - self.y) ** 2
       if distance < (PIXEL_PER_METER * 10) ** 2 :
           self.dir = math.atan2(player.y - self.y, player.x - self.x)
           return BehaviorTree.SUCCESS
       else :
           self.speed = 0
           return BehaviorTree.FAIL

    def move_to_player(self):
        self.speed = RUN_SPEED_PPS
        return BehaviorTree.SUCCESS

    def build_behavior_tree(self):
        wander_node = LeafNode("Wander", self.wander)
        find_player_node = LeafNode("Find Player", self.find_player)
        move_to_player_node = LeafNode("Move to Player", self.move_to_player)
        chase_node = SequenceNode("Chase")
        chase_node.add_children(find_player_node, move_to_player_node)
        wander_chase_node = SelectorNode("WanderChase")
        wander_chase_node.add_children(chase_node, wander_node)
        self.bt = BehaviorTree(wander_chase_node)

    def update(self):
        self.bt.run()
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % FRAMES_PER_ACTION
        self.x += self.speed * math.cos(self.dir) * game_framework.frame_time
        self.y += self.speed * math.sin(self.dir) * game_framework.frame_time

        self.x = clamp(50, self.x, 1280 - 50)
        self.y = clamp(50, self.y, 1024 - 50)

    def draw(self) :
        if math.cos(self.dir) < 0:
            self.image.clip_draw(int(self.frame) * 78, 98, 78, 98, self.x, self.y)
        else :
            self.image.clip_draw(int(self.frame) * 78, 0, 78, 98, self.x, self.y)
        draw_rectangle(*self.get_bb())

    def get_bb(self) :
        return self.x - 30, self.y - 50, self.x + 30, self.y + 50

    def handle_event(self, event):
        pass



