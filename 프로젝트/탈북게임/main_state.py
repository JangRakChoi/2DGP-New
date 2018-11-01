import random
import json
import os

from pico2d import *
import game_framework
import game_world
import FailState

from Player import Player
from Map3 import Map
from Enemy import Enemy

name = "MainState"

player = None
enemy = None

def enter():
    global player
    player = Player()
    map = Map()
    enemy = Enemy()
    game_world.add_object(map, 0)
    game_world.add_object(player, 1)
    game_world.add_object(enemy, 1)


def exit():
    game_world.clear()

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
        elif player.hp < 0 :
            game_framework.run(FailState)
        else:
            player.handle_event(event)


def update():
    for game_object in game_world.all_objects():
        game_object.update()
    if collide(player, enemy):
        player.hp -= 10

def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()

def collide(a, b) :
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b : return False
    if right_a < left_b : return False
    if top_a < bottom_b : return False
    if bottom_a > top_b : return False

    return True













