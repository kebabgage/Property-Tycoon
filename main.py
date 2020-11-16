import pygame
from game import Game
import buttons
import GUI
import tile
import time
import bidder
import player
import ai
import actions
import random
import card
pygame.init()

def main():
    # init game
    game = Game()
    board = game.get_board()

    # iterate over players
    while not game.is_over():
        # do this while the turn is still going on
        while game.get_turns().status():
            if game.current_player()._ai:
                game.current_player().act(game)
            else:
                rolling_phase(game)
                action_phase(game)
                end_phase(game)

        # set current player to next player; set status to True again
        game.get_turns().next()
        if game.get_turns()._go_again:
            game.get_turns().go_again()

# add ai jail
# add ai bidding

def jail_phase(game):
    board = game.get_board()
    display = board.get_display()
    current_player = game.get_turns().current()
    bailed = False

    while True:

        game.draw()
        if current_player.jail_card:
            card.display_jail_card(display)

        buttons.button_bail.show(display)
        pygame.display.update()

        for event in pygame.event.get():
            check_quit(event)
            check_concede(event, game)
            x,y = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN and buttons.button_bail.over():
                buttons.button_bail_function(game)
                return "End Bail Phase"
            if event.type == pygame.MOUSEBUTTONDOWN and card.JAIL_CARD_RECT.collidepoint(x,y):
                actions.use_jail_card(game)
                return "Used Card"

def rolling_phase(game):
    board = game.get_board()
    display = board.get_display()
    current_player = game.get_turns().current()

    if current_player.inJail:
        jail_phase(game)
    else:
        while True:
            if current_player.isBankrupt:
                return None
            for event in pygame.event.get():
                check_quit(event)
                check_concede(event, game)
                if event.type == pygame.MOUSEBUTTONDOWN and buttons.button_roll.over():
                    buttons.button_roll_function(game)
                    return "End Rolling Phase"

            game.draw()
            buttons.button_roll.show(display)
            pygame.display.update()

def action_phase(game):
    board = game.get_board()
    display = board.get_display()
    passed = False

    current_player = game.get_turns().current()
    current_position = current_player.getPosition()
    current_tile = game.get_board().get_tile_at(current_position)
    paid_rent = False
    bought_something = False

    while not passed:
        if current_player.isBankrupt:
            return "end"

        game.draw()

        mode = 0

        if type(current_tile) == tile.PropertyTile:
            # player owns the current tile
            if current_tile._owner == current_player:
                mode = 0
                buttons.button_end_turn.show(display)
            # No one owns the current tile
            elif current_tile._owner.getPlayerName() == "The Bank" and current_player._passed_go_once:
                mode = 1
                buttons.button_buy.show(display)
                buttons.button_end_turn.show(display)
            elif current_tile._owner.getPlayerName() == "The Bank" and not current_player._passed_go_once:
                mode = 0
                buttons.button_end_turn.show(display)
            else:
                mode = 2
                if not paid_rent:
                    buttons.button_pay_rent.show(display)
                buttons.button_end_turn.show(display)

        if type(current_tile) == tile.ActionTile:
                mode = 3
                buttons.button_end_turn.show(display)

        # current tile is an Action Tile
        if type(current_tile) == tile.ActionTile:
            pass

        for event in pygame.event.get():
            check_quit(event)
            check_concede(event, game)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mode == 0:
                    if buttons.button_end_turn.over():
                        return "end turn"
                if mode == 1:
                    if buttons.button_buy.over():
                        buttons.button_buy_function(game)
                        bought_something = True
                    if buttons.button_end_turn.over():
                        return buttons.button_end_turn_function(game, bought_something)
                if mode == 2:
                    if buttons.button_pay_rent.over():
                        if paid_rent == False:
                            buttons.button_pay_rent_function(game)
                            paid_rent = True
                    if buttons.button_end_turn.over():
                        if paid_rent:
                            return "end turn"
                if mode == 3:
                    if buttons.button_end_turn.over():
                        return "end turn"

        pygame.display.update()

def end_phase(game):
    current_player = game.current_player()
    actions.bankruptcy_check(game)

    if current_player.isBankrupt:
        print("bankrupt: ", current_player.getPlayerName())
        game.remove_current_player()
        return 0
    else:
        if game.get_turns()._go_again:
            game.get_turns().previous()
        game.get_turns().end_turn()

def check_quit(event):
    if event.type == pygame.QUIT:
        pygame.quit()
        quit()

def check_concede(event, game):
    if event.type == pygame.MOUSEBUTTONDOWN:
        if buttons.button_concede.over():
            buttons.button_concede_function(game)

if __name__ == '__main__':
    main()
