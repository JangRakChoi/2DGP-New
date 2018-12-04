from pico2d import *
import game_framework
import main_state

name = "StartState"
image = None
logo_time = 0.0
bgm = None

stage_num = 0

Siren_bgm = None

def enter():
    global image
    image = load_image('start.png')

    global bgm
    bgm = load_music('TheTorchOfTheAnnihilationOfCommunism.mp3')
    bgm.set_volume(100)
    bgm.repeat_play()



def exit():
    global image
    del(image)

    global Siren_bgm
    Siren_bgm = load_music('SIREN.mp3')
    Siren_bgm.set_volume(100)
    Siren_bgm.repeat_play()

def update():
    pass

def draw():
    global image
    clear_canvas()
    image.draw(640, 560)
    update_canvas()

def handle_events():
    events = get_events()
    for event in events :
        if event.type == SDL_QUIT :
            game_framework.quit()
        else :
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE) :
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                game_framework.change_state(main_state)

