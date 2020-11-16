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

class Game:

    def __init__(self, test=False):

        self._players = []
        self._tokens = ["boot", "phone", "hat", "cat", "goblet", "spoon"]

        self._MUSIC = True
        self._TESTING = test

        self.play_intro()

        self._turns = TurnManager(self._players)
        self._board = Board()
        self._board.setup_board()
        self._bank = Bank()

        self._is_over = False
        self._winner = None

        #cards
        self._pot_luck, self._opp_knocks = create_game_decks(self)
        self._pot_luck.shuffle()
        self._opp_knocks.shuffle()


        self._last_roll = 0
        self._free_parking = 0

    def play_intro(self):

        if self._MUSIC:
            pygame.mixer.music.load("soundtrack.ogg")
            pygame.mixer.music.play(-1)

        if self._TESTING:
            num_players = 3

            self._players.append(Player("Ege", "boot"))
            self._players.append(Player("Evan", "phone"))
            #self._players.append(Player("Kingsley", "hat"))

            #self._players.append(ai.AI("bot1", "boot"))
            #self._players.append(ai.AI("bot2", "phone"))
            self._players.append(ai.AI("bot3", "hat"))

            self._mode = ["Full", "Abridged"][1]
            self._clock = clock.Clock()
            self._clock.set_time_limit("0:10:00")

        else:
            num_players = GUI.game_intro()
            player_names, ai_info = GUI.select(num_players)
            for i in range(len(player_names)):
                player_name = player_names[i]
                new_token = self._tokens[i]
                if ai_info[i] == 0:
                    new_player = Player(player_name, new_token)
                else:
                    new_player = ai.AI(player_name, new_token)

                self._players.append(new_player)

            selected_mode, selected_duration = GUI.mode_select()
            self._mode = selected_mode
            self._clock = clock.Clock()
            self._clock.set_time_limit(selected_duration)

    def get_players(self):
        return self._players

    def get_board(self):
        return self._board

    def get_bank(self):
        return self._bank

    def get_player(self, key):
        return self._players[key]

    def current_player(self):
        return self._turns.current()

    def get_next_player(self):
        return self._turns.next()

    def get_turns(self):
        return self._turns

    def is_over(self):
        return self._is_over

    def remove_current_player(self):
        self._turns.remove_current_player()

    def get_display(self):
        return self.get_board().get_display()

    def get_opportunity_deck(self):
        return self._opp_knocks

    def get_pot_luck_deck(self):
        return self._pot_luck

    def draw(self):
        """
        Do this every frame.
        """
        self._board.draw_board(self)
        self.check_termination()

    def terminate(self):
        # pick winner
        winner_name = self.pick_winner().getPlayerName()

        while True:
        # message
            display = self.get_display()

            # background
            display.fill((20,20,20))

            # crown
            crown_image = pygame.image.load("GUI/images/crown.png")
            display.blit(crown_image, (400, 100))

            # winner text
            out_string = winner_name
            x,y = pygame.mouse.get_pos()
            out_text = GUI.GameText((500,500), out_string, (255,255,255), 85)
            out_text.textRect.center = (715,580)

            out_text.show(display)

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    print(x,y)
                if event.type == pygame.QUIT:
                    quit()
                    pygame.quit()

            pygame.display.update()



    def pick_winner(self):
        max_asset = 0
        winner = self._players[0]
        for p in self._players:
            assets = p.calculate_assets()
            if assets > max_asset:
                winner = p
                max_asset = assets
        return winner

    def check_termination(self):
        if len(self._players) == 1:
            self.terminate()
        if self._mode == "Abridged":
            if self._clock.abridged_check(self):
                self.terminate()

def create_game_decks(game):

    opportunity_knocks = []
    pot_luck = []

    with open("CardData.json", "r") as read_file:
        data = json.load(read_file)

    for portion in data:
        card_id = portion['Card_ID']
        subclass = portion["SubClassType"]
        desc = portion["Description"]
        action = portion["ActionData"]
        card_type = portion["Card Type"]
        image_path = portion["Image"]

        new_card = None

        if portion['SubClassType'] == "Payment":
            # print(card_id, card_type, desc, action, game)
            new_card = PaymentCard(card_id, card_type, desc, action, game, image_path)

        elif portion['SubClassType'] == "Movement":
            new_card = MovementCard(card_id, card_type, desc, action, game, image_path)

        elif portion['SubClassType'] == "JailFree":
            new_card = JailFreeCard(card_id, card_type, desc, action, game, image_path)

        elif portion['SubClassType'] == "Repair":
            new_card = RepairCard(card_id, card_type, desc, action, game, image_path)


        if new_card.get_type() == "Opportunity knocks":
            opportunity_knocks.append(new_card)
        elif new_card.get_type() == "Pot luck":
            pot_luck.append(new_card)

    opportunity_knocks_deck = Deck(opportunity_knocks)
    pot_luck_deck = Deck(pot_luck)
    return (opportunity_knocks_deck, pot_luck_deck)

if __name__ == "__main__":

    # #
    # token_list = ['!', '@', '#', '$', '%', '^']
    # # How many players do we want
    # player_count = input("How many players are playing?  ")
    #
    # # Check that player count is not greater than 6
    # while int(player_count) < 2 or int(player_count) > 6:
    #     print("This game is for between 2 and 6 players. ")
    #     player_count = input("How many players are playing?  ")

    player_list = [Player("Kaleb", "1"), Player("Geg", "!")]

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
