from pico2d import *
import game_framework
import start_state
import game_world

name = "FailState"
image = None
logo_time = 0.0
bgm = None

def enter():
    global image, bgm
    image = load_image('Fail.png')
    start_state.Siren_bgm.stop()

    bgm = load_music('ENDING.mp3')
    bgm.set_volume(100)
    bgm.repeat_play()


def exit():
    global image
    del(image)

def update():
    pass

def draw():
    global image
    clear_canvas()
    image.draw(640, 512)
    update_canvas()

def handle_events():
    events = get_events()
    for event in events :
        if event.type == SDL_QUIT :
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:

            game_framework.quit()

