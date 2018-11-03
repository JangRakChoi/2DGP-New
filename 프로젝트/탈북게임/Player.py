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

RIGHT_DOWN, LEFT_DOWN, UP_DOWN, DOWN_DOWN, RIGHT_UP, LEFT_UP, UP_UP, DOWN_UP ,SHIFT_UP, SHIFT_DOWN, SHIFT_TIMER = range(11)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
    (SDL_KEYDOWN, SDLK_UP): UP_DOWN,
    (SDL_KEYDOWN, SDLK_DOWN): DOWN_DOWN,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
    (SDL_KEYUP, SDLK_LEFT): LEFT_UP,
    (SDL_KEYUP, SDLK_UP): UP_UP,
    (SDL_KEYUP, SDLK_DOWN): DOWN_UP,
    (SDL_KEYDOWN, SDLK_LSHIFT): SHIFT_DOWN,
    (SDL_KEYUP, SDLK_LSHIFT): SHIFT_UP
}

class IdleState:
    @staticmethod
    def enter(boy, event):
        if event == RIGHT_DOWN:
            boy.velocityRL += WALK_SPEED_PPS
        elif event == LEFT_DOWN:
            boy.velocityRL -= WALK_SPEED_PPS
        elif event == RIGHT_UP:
            boy.velocityRL -= WALK_SPEED_PPS
        elif event == LEFT_UP:
            boy.velocityRL += WALK_SPEED_PPS
        elif event == UP_DOWN:
            boy.velocityUD += WALK_SPEED_PPS
        elif event == UP_UP:
            boy.velocityUD -= WALK_SPEED_PPS
        elif event == DOWN_UP:
            boy.velocityUD += WALK_SPEED_PPS
        elif event == DOWN_DOWN:
            boy.velocityUD -= WALK_SPEED_PPS
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
        if boy.hide == False :
            if boy.dirx == 1 or boy.diry == 1:
                boy.image.clip_draw(int(boy.frame) * 125, 300, 125, 100, boy.x, boy.y)
            else:
                boy.image.clip_draw(int(boy.frame) * 125, 200, 125, 100, boy.x, boy.y)

class WalkState :
    @staticmethod
    def enter(boy, event):
        if event == RIGHT_DOWN:
            boy.velocityRL += WALK_SPEED_PPS
        elif event == LEFT_DOWN:
            boy.velocityRL -= WALK_SPEED_PPS
        elif event == RIGHT_UP:
            boy.velocityRL -= WALK_SPEED_PPS
        elif event == LEFT_UP:
            boy.velocityRL += WALK_SPEED_PPS
        elif event == UP_DOWN:
            boy.velocityUD += WALK_SPEED_PPS
        elif event == UP_UP:
            boy.velocityUD -= WALK_SPEED_PPS
        elif event == DOWN_UP:
            boy.velocityUD += WALK_SPEED_PPS
        elif event == DOWN_DOWN:
            boy.velocityUD -= WALK_SPEED_PPS
        boy.dirx = clamp(-1, boy.dirx, 1)
        boy.diry = clamp(-1, boy.diry, 1)

    @staticmethod
    def exit(boy, event):
        pass

    @staticmethod
    def do(boy):
        boy.frame = (boy.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8
        boy.x += boy.velocityRL * game_framework.frame_time
        boy.y += boy.velocityUD * game_framework.frame_time
        boy.x = clamp(25, boy.x, 1280 - 25)
        boy.y = clamp(25, boy.y, 1000 - 25)

    @staticmethod
    def draw(boy):
        if boy.hide == False:
            if boy.dirx == 1 or boy.diry == 1:
                boy.image.clip_draw(int(boy.frame) * 125, 100, 125, 100, boy.x, boy.y)
            else:
                boy.image.clip_draw(int(boy.frame) * 125, 0, 125, 100, boy.x, boy.y)


class RunState:

    @staticmethod
    def enter(boy, event):
        if event == RIGHT_DOWN:
            boy.velocityRL += WALK_SPEED_PPS
        elif event == LEFT_DOWN:
            boy.velocityRL -= WALK_SPEED_PPS
        elif event == RIGHT_UP:
            boy.velocityRL -= WALK_SPEED_PPS
        elif event == LEFT_UP:
            boy.velocityRL += WALK_SPEED_PPS
        elif event == UP_DOWN:
            boy.velocityUD += WALK_SPEED_PPS
        elif event == UP_UP:
            boy.velocityUD -= WALK_SPEED_PPS
        elif event == DOWN_UP:
            boy.velocityUD += WALK_SPEED_PPS
        elif event == DOWN_DOWN:
            boy.velocityUD -= WALK_SPEED_PPS
        boy.dirx = clamp(-1, boy.dirx, 1)
        boy.diry = clamp(-1, boy.diry, 1)
        boy.timer = 100

    @staticmethod
    def exit(boy, event):
        pass

    @staticmethod
    def do(boy):
        boy.frame = (boy.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8
        boy.x += boy.velocityRL * game_framework.frame_time
        boy.y += boy.velocityUD * game_framework.frame_time
        boy.x = clamp(25, boy.x, 1280 - 25)
        boy.y = clamp(25, boy.y, 1000 - 25)
        boy.timer -= 1
        if boy.timer == 0:
            boy.add_event(SHIFT_TIMER)

    @staticmethod
    def draw(boy):
        if boy.dirx == 1 or boy.diry == 1 :
            boy.image.clip_draw(int(boy.frame) * 125, 100, 125, 100, boy.x, boy.y)
        else:
            boy.image.clip_draw(int(boy.frame) * 125, 0, 125, 100, boy.x, boy.y)

next_state_table = {
    IdleState: {RIGHT_UP: WalkState, LEFT_UP: WalkState, RIGHT_DOWN: WalkState, LEFT_DOWN: WalkState, UP_DOWN: WalkState, DOWN_DOWN: WalkState, UP_UP: WalkState, DOWN_UP: WalkState, SHIFT_DOWN: IdleState, SHIFT_UP: IdleState },
    RunState: {SHIFT_TIMER: WalkState, SHIFT_UP: WalkState, SHIFT_DOWN: RunState, RIGHT_UP: IdleState, LEFT_UP: IdleState,
                RIGHT_DOWN: IdleState, LEFT_DOWN: IdleState, UP_DOWN: IdleState, DOWN_DOWN: IdleState, UP_UP: IdleState, DOWN_UP: IdleState },
    WalkState: {RIGHT_UP: IdleState, LEFT_UP: IdleState, LEFT_DOWN: IdleState, RIGHT_DOWN: IdleState, UP_DOWN: IdleState, DOWN_DOWN: IdleState,
                UP_UP: IdleState, DOWN_UP: IdleState, SHIFT_DOWN : RunState, SHIFT_UP : WalkState},
}

class Player:
    def __init__(self) :
        self.image = load_image("animation_sheet.png")
        self.x, self.y = 100, 300
        self.frame = 0
        self.hp = 100
        self.velocityRL = 0
        self.velocityUD = 0
        self.dirx = 1
        self.diry = 1
        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter(self, None)
        self.time = 0
        self.where_collide = 0
        self.hide = False

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
        return self.x - 25, self.y - 50, self.x + 25, self.y + 50

    def collide_enemy(self) :
        self.hp -= 10
        if self.where_collide == 1 :
            self.x -= 20
        if self.where_collide == 2 :
            self.y -= 20
        if self.where_collide == 3 :
            self.x += 20
        if self.where_collide == 4 :
            self.y += 20

    def collide_tree(self) :
        if self.where_collide == 1 :
            self.x -= 10
        if self.where_collide == 2 :
            self.y -= 10
        if self.where_collide == 3 :
            self.x += 10
        if self.where_collide == 4 :
            self.y += 10