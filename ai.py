import pygame
import player
import buttons
import GUI
import tile
import time
import bidder
import card
import actions
import random

pygame.init()
class AI(player.Player):
    def __init__(self, name, token):
        super().__init__(name, token)
        self._ai = True


    def ai_roll(self, game):
        board = game.get_board()
        display = board.get_display()
        current_player = game.get_turns().current()

        if current_player.inJail:
            self.ai_jail(game)
        else:
            if current_player.isBankrupt:
                return None

            game.draw()
            buttons.button_roll.show(display)
            pygame.display.update()

            time.sleep(1)

            buttons.button_roll_function(game)

            return "End Rolling Phase"

    def ai_end(self, game):
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


    def ai_action(self, game):
        board = game.get_board()
        display = board.get_display()
        passed = False

        current_player = game.get_turns().current()
        current_position = current_player.getPosition()
        current_tile = game.get_board().get_tile_at(current_position)
        paid_rent = False
        bought_something = False

        game.draw()

        if current_player.isBankrupt:
            return "end"

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

        pygame.display.update()
        time.sleep(1)

        # current tile is an Action Tile
        if type(current_tile) == tile.ActionTile:
            pass
        if mode == 0:
            time.sleep(1)
            buttons.button_end_turn_function(game, bought_something)
            pygame.display.update()
            return "end turn"
        if mode == 1:
            time.sleep(1)
            p = random.randint(0,2)
            #if p == 0 or p == 1:
            if p == 0 or p == 1 or p == 2:
                buttons.button_buy_function(game)
                bought_something = True
            pygame.display.update()
            time.sleep(1)
            return buttons.button_end_turn_function(game, bought_something)
        if mode == 2:
            time.sleep(1)
            buttons.button_pay_rent_function(game)
            pygame.display.update()
            time.sleep(1)
            buttons.button_end_turn.over()
        if mode == 3:
            pygame.display.update()
            time.sleep(1)
            return "end turn"


    def ai_jail(self, game):
        board = game.get_board()
        display = board.get_display()
        current_player = game.get_turns().current()

        game.draw()
        if current_player.jail_card:
            card.display_jail_card(display)
        buttons.button_bail.show(display)
        pygame.display.update()
        time.sleep(2)

        if current_player.jail_card:
            actions.use_jail_card(game)
        else:
            buttons.button_bail_function(game)

        pygame.display.update()
        time.sleep(1)
        return "End jail phase"

    def act(self, game):
        self.ai_roll(game)
        self.ai_action(game)
        self.ai_end(game)
