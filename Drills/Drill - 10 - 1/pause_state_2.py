import game_framework
from pico2d import *
import main_state_2

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
    frame = (frame + 1) % 100

def draw():
    global frame
    clear_canvas()
    main_state_2.grass.draw()
    main_state_2.boy.draw()
    if (frame % 100 < 50) :
        image.clip_draw(250, 250, 400, 400, 800 // 2, 600 // 2)
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


def pause(): pass


def resume(): pass

