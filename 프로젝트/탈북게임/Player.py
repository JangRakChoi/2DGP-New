from pico2d import *
import game_world
import random

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

class Player:
    def __init__(self) :
        self.image = load_image("player.png")
        self.x, self.y = 0, 300
        self.frame = 0
        self.hp = 100
        self.velocityRL = 0
        self.velocityUD = 0

    def draw(self) :
        if (self.velocityRL == 0 and self.velocityUD == 0) :
            self.image.clip_draw(0, 100, 100, 100, self.x, self.y)
        elif (self.velocityRL > 0) :
            self.image.clip_draw(self.frame * 100, 100, 100, 100, self.x, self.y)
        else :
            self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)

    def update(self) :
        self.frame = (self.frame + 1) % 8
        self.x += self.velocityRL * 3
        self.y += self.velocityUD * 3
        self.x = clamp(50, self.x, 1280 - 50)
        self.y = clamp(50, self.y, 1024 - 50)

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

    def get_bb(self) :
        return self.x - 50, self.y - 50, self.x + 50, self.y + 50