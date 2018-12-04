import game_framework
from pico2d import *
import FailState

name = "pause_state_2"
image = None
frame = 0

def enter():
    global image
    image = load_image('pause.png')

def exit():
    global image
    del (image)

def update():
    global frame
    frame = (frame + 1) % 300

def draw():
    global frame
    clear_canvas()
    image.draw(640, 540)
    update_canvas()

def handle_events():
    global frame
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_p:
            game_framework.pop_state()
            frame = 0
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE :
            game_framework.run(FailState)


def pause(): pass


def resume(): pass

