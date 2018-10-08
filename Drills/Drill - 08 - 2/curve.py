from pico2d import *
import random

KPU_WIDTH, KPU_HEIGHT = 1280, 1024

open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')

frame, x, y, temp = 0, 0, 0, 0
running = True
xPos = [random.randint(0, 1280 - 20) for n1 in range(10)]
yPos = [random.randint(0, 1024 - 20) for n2 in range(10)]

def Draw(x, y) :
    pass

while running :
    pass

close_canvas()
