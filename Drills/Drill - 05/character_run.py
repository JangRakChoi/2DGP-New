from pico2d import *
open_canvas()
grass = load_image('grass.png')
character = load_image('animation_sheet.png')

def StopRightSide(x, y) :
    clear_canvas()
    grass.draw(400, 30)
    character.clip_draw(0, 300, 100, 100, x, y)
    update_canvas()
    delay(0.2)

def StopLeftSide(x, y) :
    clear_canvas()
    grass.draw(400, 30)
    character.clip_draw(0, 200, 100, 100, x, y)
    update_canvas()
    delay(0.2)

def MoveFirstStep() :
    frame, x, y = 0, 203, 535
    while (x > 132) :
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 0, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        x -= 5
        delay(0.01)
        get_events()

    while (y > 243) :
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 100, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        y -= 5
        delay(0.01)
        get_events()

    StopRightSide(x, y)

def MoveSecondStep() :
    frame, x, y = 0, 132, 243
    while (x < 535):
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 100, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        x += 5
        delay(0.01)
        get_events()

    while (y < 470) :
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 0, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        y += 5
        delay(0.01)
        get_events()

    StopLeftSide(x, y)

def MoveThirdStep() :
    frame, x, y = 0, 535, 470
    while (x > 477):
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 0, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        x -= 5
        delay(0.01)
        get_events()

    while (y > 203) :
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 100, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        y -= 5
        delay(0.01)
        get_events()

    StopRightSide(x, y)

def MoveFourthStep() :
    pass

def MoveFifthStep() :
    pass

def MoveSixthStep() :
    pass

def MoveSeventhStep() :
    pass

def MoveEighthStep() :
    pass

def MoveninthStep() :
    pass

def MovetenthStep() :
    pass

while True :
    #MoveFirstStep()
    #MoveSecondStep()
    MoveThirdStep()
    MoveFourthStep()
    MoveFifthStep()
    MoveSixthStep()
    MoveSeventhStep()
    MoveEighthStep()
    MoveninthStep()
    MovetenthStep()

close_canvas()