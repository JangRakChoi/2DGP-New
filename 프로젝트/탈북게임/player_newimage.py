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

WALK_SPEED_KMPH = 4.0
WALK_SPEED_MPM = (WALK_SPEED_KMPH * 1000.0 / 60.0)
WALK_SPEED_MPS = (WALK_SPEED_MPM / 60.0)
WALK_SPEED_PPS = (WALK_SPEED_KMPH * PIXEL_PER_METER)

# Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8

RIGHTKEY_DOWN, LEFTKEY_DOWN, UPKEY_DOWN, DOWNKEY_DOWN, RIGHTKEY_UP, LEFTKEY_UP, UPKEY_UP, DOWNKEY_UP, SPACE = range(9)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHTKEY_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFTKEY_DOWN,
    (SDL_KEYDOWN, SDLK_UP): UPKEY_DOWN,
    (SDL_KEYDOWN, SDLK_DOWN): DOWNKEY_DOWN,
    (SDL_KEYUP, SDLK_RIGHT): RIGHTKEY_UP,
    (SDL_KEYUP, SDLK_LEFT): LEFTKEY_UP,
    (SDL_KEYUP, SDLK_UP): UPKEY_UP,
    (SDL_KEYUP, SDLK_DOWN): DOWNKEY_UP,
    (SDL_KEYDOWN, SDLK_SPACE): SPACE
}

class WalkingState :
    @staticmethod
    def enter(boy, event):
        if event == RIGHTKEY_DOWN:
            boy.x_velocity += WALK_SPEED_PPS
        elif event == RIGHTKEY_UP:
            boy.x_velocity -= WALK_SPEED_PPS
        if event == LEFTKEY_DOWN:
            boy.x_velocity -= WALK_SPEED_PPS
        elif event == LEFTKEY_UP:
            boy.x_velocity += WALK_SPEED_PPS

        if event == UPKEY_DOWN:
            boy.y_velocity += WALK_SPEED_PPS
        elif event == UPKEY_UP:
            boy.y_velocity -= WALK_SPEED_PPS
        if event == DOWNKEY_DOWN:
            boy.y_velocity -= WALK_SPEED_PPS
        elif event == DOWNKEY_UP:
            boy.y_velocity += WALK_SPEED_PPS

    @staticmethod
    def exit(boy, event):
        pass

    @staticmethod
    def do(boy):
        boy.frame = (boy.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % FRAMES_PER_ACTION
        boy.x += boy.x_velocity * game_framework.frame_time
        boy.y += boy.y_velocity * game_framework.frame_time
        #boy.x = clamp(25, boy.x, get_canvas_width() - 25)
        #boy.y = clamp(25, boy.y, get_canvas_height() - 25)
        boy.x = clamp(25, boy.x, 1280 - 50)
        boy.y = clamp(25, boy.y, 1080 - 50)
        boy.timer += get_time() - boy.cur_time
        boy.cur_time = get_time()
        if boy.collideWithEnemy == True :
            if boy.timer >= 3:
                boy.collideWithEnemy = False
                boy.image.opacify(1)
                boy.timer = 0

    @staticmethod
    def draw(boy):
        if boy.hide == False:
            if boy.collideWithEnemy == True:
                boy.image.opacify(random.randint(1, 100) * 0.01)
            if boy.x_velocity > 0:
                boy.image.clip_draw(int(boy.frame) * 100, 100, 100, 100, boy.x, boy.y)
                boy.dir = 1
            elif boy.x_velocity < 0:
                boy.image.clip_draw(int(boy.frame) * 100, 0, 100, 100, boy.x, boy.y)
                boy.dir = -1
            else:
                # if boy x_velocity == 0
                if boy.y_velocity > 0 or boy.y_velocity < 0:
                    if boy.dir == 1:
                        boy.image.clip_draw(int(boy.frame) * 100, 100, 100, 100, boy.x, boy.y)
                    else:
                        boy.image.clip_draw(int(boy.frame) * 100, 0, 100, 100, boy.x, boy.y)
                else:
                    # boy is idle
                    if boy.dir == 1:
                        boy.image.clip_draw(0, 100, 100, 100, boy.x, boy.y)
                    else:
                        boy.image.clip_draw(700, 0, 100, 100, boy.x, boy.y)

#next_state_table = {
#    IdleState: {RIGHT_UP: WalkState, LEFT_UP: WalkState, RIGHT_DOWN: WalkState, LEFT_DOWN: WalkState, UP_DOWN: WalkState, DOWN_DOWN: WalkState, UP_UP: WalkState, DOWN_UP: WalkState, SHIFT_DOWN: IdleState, SHIFT_UP: IdleState },
#    RunState: {SHIFT_TIMER: WalkState, SHIFT_UP: WalkState, SHIFT_DOWN: RunState, RIGHT_UP: IdleState, LEFT_UP: IdleState,
#                RIGHT_DOWN: IdleState, LEFT_DOWN: IdleState, UP_DOWN: IdleState, DOWN_DOWN: IdleState, UP_UP: IdleState, DOWN_UP: IdleState },
#    WalkState: {RIGHT_UP: IdleState, LEFT_UP: IdleState, LEFT_DOWN: IdleState, RIGHT_DOWN: IdleState, UP_DOWN: IdleState, DOWN_DOWN: IdleState,
#                UP_UP: IdleState, DOWN_UP: IdleState, SHIFT_DOWN : RunState, SHIFT_UP : WalkState},
#}

next_state_table = {
    WalkingState: {RIGHTKEY_UP: WalkingState, LEFTKEY_UP: WalkingState, RIGHTKEY_DOWN: WalkingState, LEFTKEY_DOWN: WalkingState,
                UPKEY_UP: WalkingState, UPKEY_DOWN: WalkingState, DOWNKEY_UP: WalkingState, DOWNKEY_DOWN: WalkingState,
                SPACE: WalkingState}
}

class Player:
    def __init__(self) :
        self.image = load_image("player.png")
        self.x, self.y = 100, 300
        self.frame = 0
        self.hp = 100
        self.x_velocity = 0
        self.y_velocity = 0
        self.dir = 1
        self.event_que = []
        self.cur_state = WalkingState
        self.cur_state.enter(self, None)
        self.timer = 0
        self.cur_time = 0
        self.where_collide = -1
        self.hide = False
        self.font = load_font('ENCR10B.TTF', 16)
        self.collideWithEnemy = False

    def draw(self) :
        self.cur_state.draw(self)
        self.font.draw(self.x - 50, self.y + 50, 'HP : %3.2f' % self.hp, (255, 0, 0))
        draw_rectangle(*self.get_bb())

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
        if self.collideWithEnemy == False :
            self.hp -= 10
            self.collideWithEnemy = True
        if self.where_collide == 1 :
            self.x -= self.x_velocity * game_framework.frame_time
        if self.where_collide == 2 :
            self.y -= self.y_velocity * game_framework.frame_time
        if self.where_collide == 3 :
            self.x += self.x_velocity * game_framework.frame_time
        if self.where_collide == 4 :
            self.y += self.y_velocity * game_framework.frame_time

    def collide_obj(self) :
        if self.where_collide == 1 :
            self.x -= self.x_velocity * game_framework.frame_time
        if self.where_collide == 2 :
            self.y -= self.y_velocity * game_framework.frame_time
        if self.where_collide == 3 :
            self.x += self.x_velocity * game_framework.frame_time
        if self.where_collide == 4 :
            self.y += self.y_velocity * game_framework.frame_time

    def init(self) :
        self.x, self.y = 100, 300
        self.frame = 0
        self.x_velocity = 0
        self.y_velocity = 0
        self.dir = 1
        self.event_que = []
        self.cur_state = WalkingState
        self.cur_state.enter(self, None)
        self.timer = 0
        self.cur_time = 0
        self.where_collide = -1
        self.hide = False
