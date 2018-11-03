from pico2d import *
import game_framework
import start_state
import game_world

name = "SuccessState"
image = None
logo_time = 0.0

def enter():
    global image
    image = load_image('success.png')

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
        else :
            if (event.type) == (SDL_KEYDOWN) :
                game_framework.quit()

