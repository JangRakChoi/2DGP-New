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
DEGREE_PER_TIME = 3.141592
ROTATE_PER_TIME = PIXEL_PER_METER * 3

# Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8

RIGHT_DOWN, LEFT_DOWN, UP_DOWN, DOWN_DOWN, RIGHT_UP, LEFT_UP, UP_UP, DOWN_UP = range(8)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
    (SDL_KEYDOWN, SDLK_UP): UP_DOWN,
    (SDL_KEYDOWN, SDLK_DOWN): DOWN_DOWN,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
    (SDL_KEYUP, SDLK_LEFT): LEFT_UP,
    (SDL_KEYUP, SDLK_UP): UP_UP,
    (SDL_KEYUP, SDLK_DOWN): DOWN_UP,
}

class IdleState:
    @staticmethod
    def enter(boy, event):
        if event == RIGHT_DOWN:
            boy.velocityRL += RUN_SPEED_PPS
        elif event == LEFT_DOWN:
            boy.velocityRL -= RUN_SPEED_PPS
        elif event == RIGHT_UP:
            boy.velocityRL -= RUN_SPEED_PPS
        elif event == LEFT_UP:
            boy.velocityRL += RUN_SPEED_PPS
        elif event == UP_DOWN:
            boy.velocityUD += RUN_SPEED_PPS
        elif event == UP_UP:
            boy.velocityUD -= RUN_SPEED_PPS
        elif event == DOWN_UP:
            boy.velocityUD += RUN_SPEED_PPS
        elif event == DOWN_DOWN:
            boy.velocityUD -= RUN_SPEED_PPS
        boy.dir = clamp(-1, boy.velocityRL, 1)
        boy.dir = clamp(-1, boy.velocityUD, 1)

        boy.timer = get_time()
        boy.cur_time = get_time()
        boy.sleep_timer = boy.timer + 10.0

    @staticmethod
    def exit(boy, event):
        pass

    @staticmethod
    def do(boy):
        boy.frame = (boy.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8
        boy.timer = get_time()

    @staticmethod
    def draw(boy):
        if boy.dir == 1:
            boy.image.clip_draw(int(boy.frame) * 100, 300, 100, 100, boy.x, boy.y)
        else:
            boy.image.clip_draw(int(boy.frame) * 100, 200, 100, 100, boy.x, boy.y)


class RunState:

    @staticmethod
    def enter(boy, event):
        if event == RIGHT_DOWN:
            boy.velocityRL += RUN_SPEED_PPS
        elif event == LEFT_DOWN:
            boy.velocityRL -= RUN_SPEED_PPS
        elif event == RIGHT_UP:
            boy.velocityRL -= RUN_SPEED_PPS
        elif event == LEFT_UP:
            boy.velocityRL += RUN_SPEED_PPS
        elif event == UP_DOWN:
            boy.velocityUD += RUN_SPEED_PPS
        elif event == UP_UP:
            boy.velocityUD -= RUN_SPEED_PPS
        elif event == DOWN_UP:
            boy.velocityUD += RUN_SPEED_PPS
        elif event == DOWN_DOWN:
            boy.velocityUD -= RUN_SPEED_PPS
        boy.dirx = clamp(-1, boy.velocityRL, 1)
        boy.diry = clamp(-1, boy.velocityUD, 1)


    @staticmethod
    def exit(boy, event):
        pass

    @staticmethod
    def do(boy):
        boy.frame = (boy.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8
        boy.x += boy.velocityRL * game_framework.frame_time
        boy.y += boy.velocityUD * game_framework.frame_time
        boy.x = clamp(25, boy.x, 1280 - 25)
        boy.y = clamp(25, boy.y, 1024 - 25)

    @staticmethod
    def draw(boy):
        if boy.dirx == 1:
            boy.image.clip_draw(int(boy.frame) * 100, 100, 100, 100, boy.x, boy.y)
        else:
            boy.image.clip_draw(int(boy.frame) * 100, 0, 100, 100, boy.x, boy.y)

next_state_table = {
    IdleState: {RIGHT_UP: RunState, LEFT_UP: RunState, RIGHT_DOWN: RunState, LEFT_DOWN: RunState, UP_DOWN: RunState, DOWN_DOWN: RunState, UP_UP: RunState, DOWN_UP: RunState },
    RunState: {RIGHT_UP: IdleState, LEFT_UP: IdleState, LEFT_DOWN: IdleState, RIGHT_DOWN: IdleState, UP_DOWN: IdleState, DOWN_DOWN: IdleState, UP_UP: IdleState, DOWN_UP: IdleState},
}

class Player:
    def __init__(self) :
        self.image = load_image("player.png")
        self.x, self.y = 0, 300
        self.frame = 0
        self.hp = 100
        self.velocityRL = 0
        self.velocityUD = 0
        self.dirx = 1
        self.diry = 1
        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter(self, None)

    def draw(self) :
        self.cur_state.draw(self)

    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self) :
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

    def get_bb(self) :
        return self.x - 50, self.y - 50, self.x + 50, self.y + 50