import random
import json
import os

from pico2d import *
import game_framework
import game_world
import FailState
import player_newimage
import SuccessState
import main_state_2
import start_state
import Pause_state

from Bush3 import Bush
from player_newimage import Player
from Enemy_Gun_stage3 import Enemy_Gun
from Enemy_Knife_stage3 import Enemy_Knife
from Map3 import Map
#from ItemSlot import ItemSlot
from Tree2 import Tree
from Box3 import Box
from Banana3 import Banana
from Key_stage_3 import  Key

name = "MainState"

player = None
enemys_gun = None
enemys_knife = None
trees = None
map = None
bushes = None
boxes = None
bananas = None
bullets = None

x = 640
y = 500
TreeCount = 0
BushCount = 0
BoxCount = 0
BananaCount = 0
KeyCount = random.randint(0, 5)

start_state.stage_num = 3

def enter():
    global player, enemys_gun, enemys_knife, trees, x, y, map, itemslot, bushes, boxes, bananas
    game_world.objects = [[], [], []]
    player = Player()
    map = Map()
    enemys_gun = [Enemy_Gun() for n in range(5)]
    enemys_knife = [Enemy_Knife() for n in range(3)]
    trees = [Tree() for n in range(23)]
    bushes = [Bush() for n in range(6)]
    boxes = [Box() for n in range(6)]
    bananas = [Banana() for n in range(4)]

    global key
    key = Key()
    game_world.add_object(key, 1)

    for enemy in enemys_gun :
        game_world.add_object(enemy, 1)
    for enemy in enemys_knife:
        game_world.add_object(enemy, 1)
    game_world.add_object(player, 1)
    for tree in trees :
        game_world.add_object(tree, 1)
    for banana in bananas :
        game_world.add_object(banana, 1)
    for bush in bushes :
        game_world.add_object(bush, 1)
    for box in boxes :
        game_world.add_object(box, 1)
    game_world.add_object(map, 0)

    player.hp = main_state_2.hp


def exit():
    game_world.clear()

def pause():
    pass

def resume():
    pass

def handle_events():
    global map, player, BushCount, TreeCount, BoxCount, KeyCount, boxes
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE :
            game_framework.run(FailState)
        elif player.hp <= 0 :
            game_framework.run(FailState)
        elif map.timer > 60.0 :
            game_framework.run(FailState)
        elif player.x > 1280 - 100 and key.collision == True :
            game_framework.run(SuccessState)
        elif map.timer > 300.0 :
            game_framework.run(FailState)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE :
            for box in boxes:
                if box.collision == True :
                    box.Attack_box()
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
    global TreeCount, BushCount, BoxCount
    for game_object in game_world.all_objects():
        game_object.update()
    for enemy in enemys_knife :
        if player.hide == False :
            if collide(player, enemy) :
                player.collide_enemy()
                print("Collision with Enemy_knife")
    for enemy in enemys_gun :
        if player.hide == False :
            if collide(player, enemy) :
                player.collide_enemy()
                print("Collision with Enemy_gun")

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
            box.collision = True
        else :
            box.collision = False

    for banana in bananas :
        if collide(player, banana) :
            banana.Collide()
            bananas.remove(banana)
            game_world.remove_object(banana)
            player.hp += 5

    if collide(player, key):
        key.Collide()
        key.collision = True

    if player.hp < 0 :
        game_framework.run(FailState)

def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()

def get_player() :
    return player