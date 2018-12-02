from pico2d import *
import main_state

class Map :
    def __init__(self) :
        self.image = load_image('map3.png')
        self.font = load_font('ENCR10B.TTF', 16)
        self.timer = 0
        global player

    def draw(self) :
        #self.image.clip_draw(int(main_state.player.x - 640), int(main_state.player.y) - 540, 1280, 1080, 640, 540)
        self.image.draw(960, 540)
        self.font.draw(50, 950, 'Time : %3.2f' % get_time(), (255, 255, 0))

    def update(self):
        self.timer = get_time()