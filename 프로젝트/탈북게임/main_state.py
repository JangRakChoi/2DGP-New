import random
import json
import os

from pico2d import *
import main_state_2
import game_framework
import game_world
import FailState
import start_state
import Pause_state

from player_newimage import Player
from Enemy_knife import Enemy_Knife
#from Map3 import Map
from Map3 import Map as Background
#from ItemSlot import ItemSlot
from Tree import Tree
from Bush import  Bush

name = "MainState"

player = None
enemys = None
trees = None
background = None
#itemslot = None
bushes = None

TreeCount = 0
BushCount = 0
hp = 0

start_state.stage_num = 1

def enter():
    global player
    player = Player()
    game_world.add_object(player, 1)

    global enemys
    enemys = [Enemy_Knife() for i in range(4)]
    game_world.add_objects(enemys, 1)

    global background
    background = Background()
    game_world.add_object(background, 0)

    #global itemslot
    #itemslot = ItemSlot()
    #game_world.add_object(itemslot, 1)

    global bushes
    bushes = [Bush() for n in range(3)]
    game_world.add_objects(bushes, 1)

    global trees
    trees = [Tree() for n in range(20)]
    game_world.add_objects(trees, 1)

def exit():
    game_world.clear()

def pause():
    pass

def resume():
    pass

def handle_events():
    global TreeCount, BushCount, BananaCount, player, background, hp
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif player.hp <= 0 :
            game_framework.run(FailState)
        elif (event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE) :
            game_framework.run(FailState)
        elif (event.type == SDL_KEYDOWN and event.key == SDLK_2) :
            TreeCount = 0
            BananaCount = 0
            BushCount = 0
            hp = player.hp
            game_framework.change_state(main_state_2)
        elif player.x > 1280 - 100 :
            TreeCount = 0
            BananaCount = 0
            BushCount = 0
            hp = player.hp
            game_framework.change_state(main_state_2)
        elif background.timer > 60.0 :
            game_framework.run(FailState)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_p :
            game_framework.push_state(Pause_state)
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

    if player.hp <= 0 :
        game_framework.run(FailState)

def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()

def get_player() :
    return player