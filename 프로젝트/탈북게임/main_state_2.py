import random
import json
import os

from pico2d import *
import game_framework
import game_world
import FailState
import player_newimage
import SuccessState
import main_state

from Bush2 import Bush
from player_newimage import Player
from enemy2 import Enemy2
from Map2 import Map
from ItemSlot import ItemSlot
from Tree2 import Tree
from Box import Box

name = "MainState"

player = None
enemys = None
trees = None
map = None
bushes = None
boxes = None

x = 640
y = 500
TreeCount = 0
BushCount = 0
BoxCount = 0

def enter():
    global player, enemys, trees, x, y, map, itemslot, bushes, boxes
    game_world.objects = [[], [], []]
    player = Player()
    map = Map()
    enemys = [Enemy2() for n in range(4)]
    itemslot = ItemSlot()
    trees = [Tree() for n in range(23)]
    bushes = [Bush() for n in range(4)]
    boxes = [Box() for n in range(5)]

    for enemy in enemys :
        game_world.add_object(enemy, 1)
    game_world.add_object(player, 1)
    for tree in trees :
        game_world.add_object(tree, 1)
    for bush in bushes :
        game_world.add_object(bush, 1)
    for box in boxes :
        game_world.add_object(box, 1)
    game_world.add_object(itemslot, 1)
    game_world.add_object(map, 0)

    player.hp = main_state.hp


def exit():
    game_world.clear()

def pause():
    pass

def resume():
    pass

def handle_events():
    global map, player, BushCount, TreeCount, BoxCount
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif player.hp < 0 :
            game_framework.run(FailState)
        elif map.timer > 60.0 :
            game_framework.run(FailState)
        elif player.x > 1280 - 50 :
            game_framework.run(SuccessState)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_1 :
            TreeCount = 0
            BushCount = 0
            BoxCount = 0
            game_framework.change_state(main_state)
        elif map.timer > 120.0 :
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
    global TreeCount, BushCount, BoxCount
    for game_object in game_world.all_objects():
        game_object.update()
    for enemy in enemys :
        if collide(player, enemy) :
            player.collide_enemy()
            print("Collision with Enemy")

    for tree in trees :
        if collide(player, tree) :
            player.collide_obj()
            print("Collision with Tree")

    player.hide = False

    for bush in bushes :
        if collide(player, bush) :
            player.hide = True
            print("player Collision with Bush")

    for box in boxes :
        if collide(player, box) :
            player.collide_obj()
            print("Collision with Tree")

    if player.hp < 0 :
        game_framework.run(FailState)

def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()