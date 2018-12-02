import game_framework
import pico2d

import start_state

pico2d.open_canvas(1280, 1080, sync=True)
game_framework.run(start_state)
pico2d.close_canvas()