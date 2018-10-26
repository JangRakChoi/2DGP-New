from pico2d import *

# Boy Event
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

# Player States
class IdleState :
    @staticmethod
    def enter(player) :
        player.frame = 0
        player.timer = 1000

    @staticmethod
    def exit(player) :
        pass

    @staticmethod
    def do(player) :
        player.frame = (player.frame + 1) % 8

    @staticmethod
    def draw(player) :
        if player.dirx == 1 or player.diry == 1:
            player.image.clip_draw(0, 100, 100, 100, player.x, player.y)
        else :
            player.image.clip_draw(700, 0, 100, 100, player.x, player.y)


class RunState :
    @staticmethod
    def enter(player) :
        player.frame = 0
        player.dirx = player.velocityRL
        player.diry = player.velocityUD

    @staticmethod
    def exit(player) :
        pass

    @staticmethod
    def do(player) :
        player.frame = (player.frame + 1) % 8
        player.x += player.velocityRL
        player.y += player.velocityUD
        player.x = clamp(50, player.x, 1280 - 50)
        player.y = clamp(50, player.y, 1024 - 50)

    @staticmethod
    def draw(player) :
        if (player.velocityRL == 1 or player.velocityUD == 1) :
            player.image.clip_draw(player.frame * 100, 100, 100, 100, player.x, player.y)
        else :
            player.image.clip_draw(player.frame * 100, 0, 100, 100, player.x, player.y)


next_state_table = {
    IdleState : {RIGHT_UP : RunState, LEFT_UP : RunState, UP_UP : RunState, DOWN_UP : RunState,
                  RIGHT_DOWN : RunState, LEFT_DOWN : RunState, UP_DOWN : RunState, DOWN_DOWN : RunState},
    RunState : {RIGHT_UP : IdleState, LEFT_UP : IdleState, UP_UP : IdleState, DOWN_UP : IdleState,
                  RIGHT_DOWN : IdleState, LEFT_DOWN : IdleState, UP_DOWN : IdleState, DOWN_DOWN : IdleState},
}

class Player:
    def __init__(self):
        self.x, self.y = 0 + 50, 1024 // 2
        self.image = load_image('player.png')
        self.dirx = 1
        self.diry = 1
        self.velocityRL = 0
        self.velocityUD = 0
        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter(self)

    def change_state(self,  state):
        self.cur_state.exit(self)
        self.cur_state = state
        self.cur_state.enter(self)


    def add_event(self, event):
        self.event_que.insert(0, event)


    def update(self):
       self.cur_state.do(self)
       if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.change_state(next_state_table[self.cur_state][event])

    def draw(self):
        self.cur_state.draw(self)

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table :
            key_event = key_event_table[(event.type, event.key)]
            if key_event == RIGHT_DOWN:
                self.velocityRL += 1
            elif key_event == LEFT_DOWN:
                self.velocityRL -= 1
            elif key_event == UP_DOWN:
                self.velocityUD += 1
            elif key_event == DOWN_DOWN:
                self.velocityUD -= 1
            elif key_event == RIGHT_UP:
                self.velocityRL -= 1
            elif key_event == LEFT_UP:
                self.velocityRL += 1
            elif key_event == UP_UP:
                self.velocityUD -= 1
            elif key_event == DOWN_UP:
                self.velocityUD += 1
            self.add_event(key_event)