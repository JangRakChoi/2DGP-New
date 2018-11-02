import random
import json
import os

from pico2d import *
import game_framework
import game_world
import FailState

from Player import Player
from Enemy import Enemy
from Map3 import Map
from ItemSlot import ItemSlot

name = "MainState"

player = None
enemy = None

def enter():
    global player, enemy
    player = Player()
    map = Map()
    enemy = Enemy()
    itemslot = ItemSlot()
    game_world.add_object(map, 0)
    game_world.add_object(player, 1)
    game_world.add_object(enemy, 1)
    game_world.add_object(itemslot, 1)


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


def collide(a, b) :
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b : return False
    if right_a < left_b : return False
    if top_a < bottom_b : return False
    if bottom_a > top_b : return False

    if a.x < b.x : a.where_collide = 1
    elif a.y < b.y : a.where_collide = 2
    elif a.x > b.x : a.where_collide = 3
    elif a.y > b.y : a.where_collide = 4

    return True

def update():
    for game_object in game_world.all_objects():
        game_object.update()
    if collide(player, enemy) :
        player.collide()
        print("Collision")

def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()














