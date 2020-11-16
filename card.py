import pygame
import actions
from copy import copy
import GUI

class Card:

    def __init__(self, card_id, card_type, description, action_data, game, image_path):
        self._card_id = card_id
        self._card_type = card_type
        self._description = description
        self._action_data = action_data
        self._game = game
        self._image = pygame.image.load(image_path)

        self._tile_dictionary = {
                "Go": 1,
                "Crapper Street": 2,
                "Pot Luck": 3,
                "Gangsters Paradise": 4,
                "Income Tax": 5,
                "Brighton Station": 6,
                "Weeping Angel": 7,
                "Opportunity Knocks": 8,
                "Potts Avenue": 9,
                "Nardole Drive": 10,
                "Jail": 11,
                "Skywalker Drive": 12,
                "Tesla Power Co": 13,
                "Wookie Hole": 14,
                "Rey Lane": 15,
                "Hove Station": 16,
                "Cooper Drive": 17,
                "Pot Luck": 18,
                "Wolowitz Street": 19,
                "Penny Lane": 20,
                "Free Parking": 21,
                "Yue Fei Square": 22,
                "Opportunity Knocks": 23,
                "Mulan Rouge": 24,
                "Han Xin Gardens": 25,
                "Falmer Station": 26,
                "Kirk Close": 27,
                "Picard Avenue": 28,
                "Edison Water": 29,
                "Crusher Creek": 30,
                "Go to Jail": 31,
                "Sirat Mews": 32,
                "Ghengis Crescent": 33,
                "Pot Luck": 34,
                "Ibis Close": 35,
                "Lewes Station": 36,
                "Opportunity Knocks": 37,
                "Hawking Way": 38,
                "Super Tax": 39,
                "Turing Heights": 40
            }

    def get_position_of_tile(self, tile_name):

        position = self._tile_dictionary[tile_name]
        return position

    def get_id(self):
        return self._card_id

    def get_type(self):
        return self._card_type

    def get_description(self):
        return self._description

    def action_data(self):
        return self._action_data

    def get_image(self):
        return self._image

    def display_card(self, display):
        display.blit(self.get_image(), (175,200))

    def get_payment_data(self, object):
        if object == "Bank":
            return None
        elif object == "Player":
            return "Player"
        elif object == "OtherPlayers":
            return "OtherPlayers"
        elif object == "FreeParking":
            return "FreeParking"


class PaymentCard(Card):

    def __init__(self, card_id, card_type, description, action_data, game, image_path):

        super().__init__(card_id, card_type, description, action_data, game, image_path)

        self._pay_from = self.get_payment_data(action_data[0])
        self._pay_to = self.get_payment_data(action_data[1])
        self._amount = int(action_data[2])

    def perform_action(self):
        if self._pay_from == "FreeParking":
            self._game._free_parking -= self._amount
        if self._pay_from == "Player":
            self._game.current_player().removeBankBalance(self._amount)
        if self._pay_from == "Bank":
            pass
        if self._pay_from == "OtherPlayers":
            other_players = copy(self._game.get_players())
            other_players.remove(self._game.current_player())
            for other_player in other_players:
                other_player.removeBankBalance(self._amount)

        if self._pay_to == "FreeParking":
            self._game._free_parking += self._amount
        if self._pay_to == "Player":
            self._game.current_player().addBankBalance(self._amount)
        if self._pay_to == "Bank":
            pass
        if self._pay_to == "OtherPlayers":
            for p in self._game.get_players().remove(self._game.current_player()):
                p.addBankBalance(self._amount)


class RepairCard(Card):

    def __init__(self, card_id, card_type, description, action_data, game, image_path):
        super().__init__(card_id, card_type, description, action_data, game, image_path)
        self._pay_from = self.get_payment_data(action_data[0])
        self._pay_to = self.get_payment_data(action_data[1])
        repair_costs = action_data[2].split('/')
        self._house_payment = int(repair_costs[0])
        self._hotel_payment = int(repair_costs[1])

    def perform_action(self):

        # cost = 0
        house_count = 0
        hotel_count = 0

        #for i in self._pay_from.get_owned_properties():
        for i in self._game.current_player().getPropertiesOwned():
            house_count += i.get_house_count()
            hotel_count += i.get_hotel_count()
            print(house_count, hotel_count)


        cost = (house_count * self._house_payment) + (hotel_count * self._hotel_payment)

class MovementCard(Card):

    def __init__(self, card_id, card_type, description, action_data, game, image_path):

        super().__init__(card_id, card_type, description, action_data, game, image_path)

    def perform_action(self):


        if self._action_data[0] == "Direct":
            new_position = self.get_position_of_tile(self._action_data[1]) - 1
            actions.teleport(self._game.current_player(), new_position)

        elif self._action_data[0] == "Direct-Go":
            new_position = self.get_position_of_tile(self._action_data[1]) - 1
            actions.teleport(self._game.current_player(), new_position)

        elif self._action_data[0] == "Non-Direct":
            current_positon = self._game.current_player().getPosition()
            new_position = (current_positon - 3) % 40
            self._game.current_player().setPosition(new_position)

        else:
            pass

        # new_position = action

class JailFreeCard(Card):

    def __init__(self, card_id, card_type, description, action_data, game, image_path):

        super().__init__(card_id, card_type, description, action_data, game, image_path)

    def perform_action(self):

        self._game.current_player().add_jail_free_card()



JAIL_CARD_IMAGE = pygame.image.load("GUI/images/card_images/card16.png")
JAIL_CARD_RECT = pygame.Rect(175,200,360,240)


def display_jail_card(display):
    display.blit(JAIL_CARD_IMAGE, (175,200))
