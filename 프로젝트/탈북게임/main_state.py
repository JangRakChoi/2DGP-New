import random
import json
import os

from pico2d import *

import game_framework

from Player import Player
from Map3 import Map
from Enemy import Enemy

name = "MainState"

enemy = None
player = None
map3 = None
font = None



def enter():
    global player, map3, enemy
    player = Player()
    enemy = Enemy()
    map3 = Map()

def exit():
    global player, map3, enemy
    del player
    del enemy
    del map3



def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                game_framework.quit()
        else:
            player.handle_event(event)

def collide(a, b) :
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b : return False
    if right_a < left_b : return False
    if top_a < bottom_b : return False
    if bottom_a > top_b : return False

    return True

def update():
    player.update()
    enemy.update()
    if collide(player, enemy) :
        player.hp -= 10


def draw():
    clear_canvas()
    map3.draw()
    player.draw()
    enemy.draw()
    update_canvas()







