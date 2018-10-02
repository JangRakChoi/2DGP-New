from pico2d import *
import random

KPU_WIDTH, KPU_HEIGHT = 1280, 1024

open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')

frame = 0
running = True

def Draw(p1, p2) :
    global frame
    for i in range(0, 100 + 1, 1):
        t = i / 100
        x = (1 - t) * p1[0] + t * p2[0]
        y = (1 - t) * p1[1] + t * p2[1]
        if (p1[0] < p2[0]):
            character.clip_draw(frame * 100, 100, 100, 100, x, y)
        else:
            character.clip_draw(frame * 100, 0, 100, 100, x, y)


size = 20
n = 1
points = [(random.randint(0, 1000), random.randint(0, 1000)) for i in range(size)]

while running :
    Draw(points[n-1], points[n])
    n = (n + 1) % size
    frame = 0

close_canvas()
