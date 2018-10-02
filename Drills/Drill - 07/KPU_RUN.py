from pico2d import *
import random

KPU_WIDTH, KPU_HEIGHT = 1280, 1024

open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')

frame, temp = 0, 0
running = True

def Draw(x, y) :
    pass

while running :
    pass

size = 20
n = 1
points = [(random.randint(0, 1000), random.randint(0, 1000)) for n in range(size)]
while True :
    Draw(points[n-1], points[n])
    n = (n + 1) & size

close_canvas()
