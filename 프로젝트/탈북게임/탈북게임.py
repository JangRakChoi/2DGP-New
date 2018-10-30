from pico2d import *
import random

open_canvas(1280, 1024)

xPos = [random.randint(900, 1280 - 100) for n1 in range(20)]
yPos = [random.randint(0, 1024 - 100) for n2 in range(20)]
t = 0
dirX = 0
dirY = 0

class Map :
    def __init__(self) :
        self.image = load_image('map3.png')
    def draw(self) :
        self.image.draw(640, 512)

class Enemy:
    def __init__(self) :
        self.image = load_image("enemy.png")
        # soldier pivot : 50X50
        self.where = random.randint(0, 3)
        self.x, self.y = random.randint(900, 1280 - 200), random.randint(0, 1024 - 200)
        self.nowX, self.nowY = 0, 0
        self.frame = random.randint(0, 5)
        self.n = 0
        self.count = random.randint(0, 19)

    def update(self) :
        self.frame = (self.frame + 1) % 6
        self.n = self.n + 1
        if (self.n > 100) :
            self.n = 0
        t = self.n / 100
        self.nowX, self.nowY = self.x, self.y
        self.x = ((-t ** 3 + 2 * t ** 2 - t) * xPos[(self.count - 3)] + (3 * t ** 3 - 5 * t ** 2 + 2) * xPos[(self.count - 2)] + (
                    -3 * t ** 3 + 4 * t ** 2 + t) * xPos[(self.count - 1)] + (t ** 3 - t ** 2) * xPos[(self.count)]) / 2
        self.y = ((-t ** 3 + 2 * t ** 2 - t) * yPos[(self.count - 3)] + (3 * t ** 3 - 5 * t ** 2 + 2) * yPos[(self.count - 2)] + (
                    -3 * t ** 3 + 4 * t ** 2 + t) * yPos[(self.count - 1)] + (t ** 3 - t ** 2) * yPos[(self.count)]) / 2
        if (self.n == 100) :
            self.count = (self.count + 1) % 20
        self.x = clamp(50, self.x, 1280 - 50)
        self.y = clamp(50, self.y, 1024 - 50)

    def draw(self) :
        if (self.nowX > self.x) :
            self.image.clip_draw(self.frame * 133, 100, 133, 100, self.x, self.y)
        elif (self.nowX <= self.x):
            self.image.clip_draw(self.frame * 133, 0, 133, 100, self.x, self.y)

class Player:
    def __init__(self) :
        self.image = load_image("player.png")
        self.x, self.y = 0, 300
        self.frame = 0
        self.hp = 100

    def draw(self) :
        if (dirX >= 0) :
            self.image.clip_draw(self.frame * 100, 100, 100, 100, self.x, self.y)
        else :
            self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)

    def update(self) :
        self.frame = (self.frame + 1) % 8
        self.x += dirX * 10
        self.y += dirY * 10
        self.x = clamp(50, self.x, 1280 - 50)
        self.y = clamp(50, self.y, 1024 - 50)

class Tree :
    def __init__(self) :
        self.image = load_image("Trees.png")
        self.x = random.randint(300, 1920 - 100)
        self.y = random.randint(0 + 100, 1080 - 100)

    def draw(self) :
        self.image.clip_draw(100, 145, 90, 140, self.x, self.y)

class Bush :
    def __init__(self) :
        self.image = load_image("bush.png")
        self.x = random.randint(100, 1920 - 100)
        self.y = random.randint(0 + 100, 1080 - 100)

    def draw(self) :
        self.image.clip_draw(0, 0, 150, 150, self.x, self.y)

class ItemSlot :
    def __init__(self) :
        self.image = load_image("ItemSlot.png")
    def draw(self) :
        self.image.draw(200, 30)
    def update(self):
        pass


running = True

def handle_events():
    global running
    global dirX
    global dirY
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dirX += 1
            elif event.key == SDLK_UP:
                dirY += 1
            elif event.key == SDLK_LEFT:
                dirX -= 1
            elif event.key == SDLK_DOWN:
                dirY -= 1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dirX -= 1
            elif event.key == SDLK_UP:
                dirY -= 1
            elif event.key == SDLK_LEFT:
                dirX += 1
            elif event.key == SDLK_DOWN:
                dirY += 1

player = Player()
enemies = [Enemy() for n3 in range(5)]
background = Map()
trees = [Tree() for n4 in range(5)]
bushes = [Bush() for n5 in range(5)]
itemslot = ItemSlot()

while running:
    handle_events()
    player.update()
    for enemy in enemies :
        enemy.update()
    clear_canvas()
    background.draw()
    player.draw()
    for enemy in enemies :
        enemy.draw()
    for tree in trees :
        tree.draw()
    for bush in bushes :
        bush.draw()
    itemslot.draw()
    update_canvas()
    delay(0.05)

close_canvas()