from pico2d import *
open_canvas()
grass = load_image('grass.png')
character = load_image('animation_sheet.png')

def StopRightSide(x, y) :
    pass

def StopLeftSide(x, y) :
    pass

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

def MoveSecondStep() :
    pass

def MoveThirdStep() :
    pass

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
    MoveFirstStep()
    MoveSecondStep()
    MoveThirdStep()
    MoveFourthStep()
    MoveFifthStep()
    MoveSixthStep()
    MoveSeventhStep()
    MoveEighthStep()
    MoveninthStep()
    MovetenthStep()

close_canvas()