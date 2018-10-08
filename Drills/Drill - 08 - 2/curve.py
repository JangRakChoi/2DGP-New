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
    global frame
    global temp
    if (temp < x):
        character.clip_draw(frame * 100, 100, 100, 100, x, y)
    else:
        character.clip_draw(frame * 100, 0, 100, 100, x, y)
    update_canvas()
    frame = (frame + 1) % 8
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    temp = x
    delay(0.05)

while running :
    # draw p1-p2
    for i in range(0, 50, 1):
        t = i / 100
        x = (2 * t ** 2 - 3 * t + 1) * xPos[0] + (-4 * t ** 2 + 4 * t) * xPos[1] + (2 * t ** 2 - t) * xPos[2]
        y = (2 * t ** 2 - 3 * t + 1) * yPos[0] + (-4 * t ** 2 + 4 * t) * yPos[1] + (2 * t ** 2 - t) * yPos[2]
        Draw(x, y)

    frame = 0
    # draw p2-p3
    for i in range(0, 100, 1):
        t = i / 100
        x = ((-t**3+2*t**2-t)*xPos[0] + (3*t**3-5*t**2+2)*xPos[1]+(-3*t**3+4*t**2+t)*xPos[2] + (t**3-t**2)*xPos[3]) / 2
        y = ((-t**3+2*t**2-t)*yPos[0] + (3*t**3-5*t**2+2)*yPos[1]+(-3*t**3+4*t**2+t)*yPos[2] + (t**3-t**2)*yPos[3]) / 2
        Draw(x, y)

close_canvas()
