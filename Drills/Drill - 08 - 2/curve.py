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
    for i in range(0, 100, 1):
        t = i / 100
        x = ((-t ** 3 + 2 * t ** 2 - t) * xPos[9] + (3 * t ** 3 - 5 * t ** 2 + 2) * xPos[0] + (
                    -3 * t ** 3 + 4 * t ** 2 + t) * xPos[1] + (t ** 3 - t ** 2) * xPos[2]) / 2
        y = ((-t ** 3 + 2 * t ** 2 - t) * yPos[9] + (3 * t ** 3 - 5 * t ** 2 + 2) * yPos[0] + (
                    -3 * t ** 3 + 4 * t ** 2 + t) * yPos[1] + (t ** 3 - t ** 2) * yPos[2]) / 2
        Draw(x, y)

    frame = 0
    # draw p2-p3
    for i in range(0, 100, 1):
        t = i / 100
        x = ((-t**3+2*t**2-t)*xPos[0] + (3*t**3-5*t**2+2)*xPos[1]+(-3*t**3+4*t**2+t)*xPos[2] + (t**3-t**2)*xPos[3]) / 2
        y = ((-t**3+2*t**2-t)*yPos[0] + (3*t**3-5*t**2+2)*yPos[1]+(-3*t**3+4*t**2+t)*yPos[2] + (t**3-t**2)*yPos[3]) / 2
        Draw(x, y)

    frame = 0
    # draw p3-p4
    for i in range(0, 100, 1):
        t = i / 100
        x = ((-t ** 3 + 2 * t ** 2 - t) * xPos[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * xPos[2] + (-3 * t ** 3 + 4 * t ** 2 + t) * xPos[3] + (t ** 3 - t ** 2) * xPos[4]) / 2
        y = ((-t ** 3 + 2 * t ** 2 - t) * yPos[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * yPos[2] + (-3 * t ** 3 + 4 * t ** 2 + t) * yPos[3] + (t ** 3 - t ** 2) * yPos[4]) / 2
        Draw(x, y)

    frame = 0
    # draw p4-p5
    for i in range(0, 100, 1):
        t = i / 100
        x = ((-t ** 3 + 2 * t ** 2 - t) * xPos[2] + (3 * t ** 3 - 5 * t ** 2 + 2) * xPos[3] + (-3 * t ** 3 + 4 * t ** 2 + t) * xPos[4] + (t ** 3 - t ** 2) * xPos[5]) / 2
        y = ((-t ** 3 + 2 * t ** 2 - t) * yPos[2] + (3 * t ** 3 - 5 * t ** 2 + 2) * yPos[3] + (-3 * t ** 3 + 4 * t ** 2 + t) * yPos[4] + (t ** 3 - t ** 2) * yPos[5]) / 2
        Draw(x, y)

    frame = 0
    # draw p5-p6
    for i in range(0, 100, 1):
        t = i / 100
        x = ((-t ** 3 + 2 * t ** 2 - t) * xPos[3] + (3 * t ** 3 - 5 * t ** 2 + 2) * xPos[4] + (-3 * t ** 3 + 4 * t ** 2 + t) * xPos[5] + (t ** 3 - t ** 2) * xPos[6]) / 2
        y = ((-t ** 3 + 2 * t ** 2 - t) * yPos[3] + (3 * t ** 3 - 5 * t ** 2 + 2) * yPos[4] + (-3 * t ** 3 + 4 * t ** 2 + t) * yPos[5] + (t ** 3 - t ** 2) * yPos[6]) / 2
        Draw(x, y)


    frame = 0
    # draw p6-p7
    for i in range(0, 100, 1):
        t = i / 100
        x = ((-t ** 3 + 2 * t ** 2 - t) * xPos[4] + (3 * t ** 3 - 5 * t ** 2 + 2) * xPos[5] + (-3 * t ** 3 + 4 * t ** 2 + t) * xPos[6] + (t ** 3 - t ** 2) * xPos[7]) / 2
        y = ((-t ** 3 + 2 * t ** 2 - t) * yPos[4] + (3 * t ** 3 - 5 * t ** 2 + 2) * yPos[5] + (-3 * t ** 3 + 4 * t ** 2 + t) * yPos[6] + (t ** 3 - t ** 2) * yPos[7]) / 2
        Draw(x, y)

    frame = 0
    # draw p7-p8
    for i in range(0, 100, 1):
        t = i / 100
        x = ((-t ** 3 + 2 * t ** 2 - t) * xPos[5] + (3 * t ** 3 - 5 * t ** 2 + 2) * xPos[6] + (-3 * t ** 3 + 4 * t ** 2 + t) * xPos[7] + (t ** 3 - t ** 2) * xPos[8]) / 2
        y = ((-t ** 3 + 2 * t ** 2 - t) * yPos[5] + (3 * t ** 3 - 5 * t ** 2 + 2) * yPos[6] + (-3 * t ** 3 + 4 * t ** 2 + t) * yPos[7] + (t ** 3 - t ** 2) * yPos[8]) / 2
        Draw(x, y)

    frame = 0
    # draw p8-p9
    for i in range(0, 100, 1):
        t = i / 100
        x = ((-t ** 3 + 2 * t ** 2 - t) * xPos[6] + (3 * t ** 3 - 5 * t ** 2 + 2) * xPos[7] + (-3 * t ** 3 + 4 * t ** 2 + t) * xPos[8] + (t ** 3 - t ** 2) * xPos[9]) / 2
        y = ((-t ** 3 + 2 * t ** 2 - t) * yPos[6] + (3 * t ** 3 - 5 * t ** 2 + 2) * yPos[7] + (-3 * t ** 3 + 4 * t ** 2 + t) * yPos[8] + (t ** 3 - t ** 2) * yPos[9]) / 2
        Draw(x, y)

    frame = 0
    # draw p9-p10
    for i in range(0, 100, 1):
        t = i / 100
        x = ((-t ** 3 + 2 * t ** 2 - t) * xPos[7] + (3 * t ** 3 - 5 * t ** 2 + 2) * xPos[8] + (-3 * t ** 3 + 4 * t ** 2 + t) * xPos[9] + (t ** 3 - t ** 2) * xPos[9]) / 2
        y = ((-t ** 3 + 2 * t ** 2 - t) * yPos[7] + (3 * t ** 3 - 5 * t ** 2 + 2) * yPos[8] + (-3 * t ** 3 + 4 * t ** 2 + t) * yPos[9] + (t ** 3 - t ** 2) * yPos[9]) / 2
        Draw(x, y)

close_canvas()
