from random import random, randint
from turn_manager import TurnManager
from player import Player
import ai
from board import Board
import GUI
import pygame
import clock
import display_token
import display_tile
from deck import *
from bank import *
from card import *
from read_json import *
from game import Game

game = Game(True)
property_ = game.get_board().get_tile_at(1)
print(property_.get_name())

property1 = game.get_board().get_tile_at(1)
property2 = game.get_board().get_tile_at(3)

listy = []
for i in game.current_player().getPropertiesOwned():
    listy.append(i.get_name())
print("Owned prop" + ", ".join(listy))
print("Add Crapper")
game.current_player().addPropertyOwned(property1)
game.current_player().addPropertyOwned(property2)
listy = []
for i in game.current_player().getPropertiesOwned():
    listy.append(i.get_name())
print("Owned prop" + ", ".join(listy))
print("Add Crapper2 ")

game.current_player().addPropertyOwned(property1)
listy = []
for i in game.current_player().getPropertiesOwned():
    listy.append(i.get_name())
print("Owned prop: " + ", ".join(listy))
# PL1 = Card(1, "You inherit unichr(163)100", ['Payment', 'Bank', 'Player', 100], 'Pot luck')
# card_action_handler(PL1, game)
'''
game.current_player().buy_house(property1)
game.current_player().buy_house(property1)
game.current_player().buy_house(property1)
game.current_player().buy_house(property1)
#game.current_player().buy_hotel(property1)

game.current_player().buy_house(property2)
game.current_player().buy_house(property2)
game.current_player().buy_house(property2)
game.current_player().buy_house(property2)
'''
#game.current_player().buy_hotel(property2)

game.current_player()

x = read_CardData()
#     print(len(x))
opp_knocks = []
pot = []


# Repair card test
# i = 0
# while i < len(opp_knocks):
#     print(i, opp_knocks[i])
#     i += 1

print("Pay")
paypay = game.get_opportunity_deck().get_card_at(0)
print(paypay.get_description())
# paypay.perform_action(game)

crapper = game.get_pot_luck_deck().get_card_at(2)
# crapper = pot[2]
print("crapper", crapper.get_description())
# print("backcard:  ", back.get_description(), back.action_data())
# print("Pos: ", game.current_player().get_position())
# game.current_player().set_position(10)
# print("Pos: ", game.current_player().get_position())
# game.current_player()
# back.perform_action()
# print("Pos: ", game.current_player().get_position())
advance_to_go = game.get_pot_luck_deck().get_card_at(7)

# advance_to_go = pot[7]
advance_to_go.perform_action()
# print("go", advance_to_go.get_description())

jail = game.get_pot_luck_deck().get_card_at(12)
jail.perform_action()
# print("jail", jail.get_description())

turing = game.get_opportunity_deck().get_card_at(2)
jail.perform_action()
# print("turing", turing.get_description())

hanxin = game.get_opportunity_deck().get_card_at(3)
hanxin.perform_action()
# print("hanxin", hanxin.get_description())

hove = game.get_pot_luck_deck().get_card_at(6)
hove.perform_action()
# print("hove", hove.get_description())

gogo = game.get_opportunity_deck().get_card_at(9)
print("AD", gogo.action_data())
# gogo = opp_knocks[9]
gogo.perform_action()
# print("gogo", gogo.get_description())

back3 = game.get_opportunity_deck().get_card_at(11)
# back3 = opp_knocks[11]
back3.perform_action()
# print("back", back3.get_description())

sky = game.get_opportunity_deck().get_card_at(12)
# sky = opp_knocks[12]
sky.perform_action()
# print("sky", sky.get_description())

game.get_opportunity_deck().get_card_at(13)
# jail = opp_knocks[13]
jail.perform_action()
# print("jail", jail.get_description())
