from pico2d import *

class Map :
    def __init__(self) :
        self.image = load_image('map2.png')
        self.font = load_font('ENCR10B.TTF', 16)
        self.timer = 0

    def draw(self) :
        self.image.draw(960, 540)
        self.font.draw(50, 950, 'Time : %3.2f' % get_time(), (255, 255, 0))

    def update(self):
        self.timer = get_time()
