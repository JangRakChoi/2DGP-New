import random
import json
import os

from pico2d import *
import main_state_2
import game_framework
import game_world
import FailState

from player_newimage import Player
from enemy1 import Enemy1
from Map3 import Map
#from ItemSlot import ItemSlot
from Tree import Tree
from Bush import  Bush
from Banana import Banana

name = "MainState"

player = None
enemys = None
trees = None
map = None
#itemslot = None
bushes = None
banana = None

x = 640
y = 500
TreeCount = 0
BushCount = 0
BananaCount = 0
hp = 0

def enter():
    global player, enemys, trees, x, y, map, itemslot, bushes, bananas
    game_world.objects = [[], [], []]
    player = Player()
    map = Map()
    enemys = [Enemy1() for n in range(2)]
    #itemslot = ItemSlot()
    bushes = [Bush() for n in range(3)]
    trees = [Tree() for n in range(20)]
    bananas = [Banana() for n in range(2)]

    for enemy in enemys :
        game_world.add_object(enemy, 1)
    game_world.add_object(player, 1)
    for tree in trees :
        game_world.add_object(tree, 1)
    #game_world.add_object(itemslot, 1)
    for banana in bananas:
        game_world.add_object(banana, 1)
    game_world.add_object(map, 0)
    for bush in bushes :
        game_world.add_object(bush, 1)

def exit():
    game_world.clear()

def pause():
    pass

def resume():
    pass

def handle_events():
    global TreeCount, BushCount, player, map, hp
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE) :
            game_framework.run(FailState)
        elif (event.type == SDL_KEYDOWN and event.key == SDLK_2) :
            TreeCount = 0
            BushCount = 0
            hp = player.hp
            game_framework.change_state(main_state_2)
        elif player.x > 1280 - 50 :
            TreeCount = 0
            BushCount = 0
            hp = player.hp
            game_framework.change_state(main_state_2)
        elif map.timer > 60.0 :
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
    global TreeCount, BushCount
    for game_object in game_world.all_objects():
        game_object.update()
    for enemy in enemys :
        if player.hide == False :
            if collide(player, enemy) :
                player.collide_enemy()
                print("player Collision with Enemy")

    for tree in trees :
        if collide(player, tree) :
            player.collide_obj()
            print("player Collision with Tree")

    player.hide = False

    for bush in bushes :
        if collide(player, bush) :
            player.hide = True
            print("player Collision with Bush")

    for banana in bananas :
        if collide(player, banana) :
            bananas.remove(banana)
            game_world.remove_object(banana)
            player.hp += 5
            print("player Collision with Item(Banana)")

    if player.hp < 0 :
        game_framework.run(FailState)

def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()