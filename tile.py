import pygame
import GUI
from player import Player


class Tile:
    """ An abstract representation of a Monopoly game tile

        Attributes:
            position: An unique integer indicating its position within the Monopoly board
            name: A unique string of the tile's name
            can_be_bought: A boolean that indicates whether this tile can be bought
            """

    def __init__(self, position, name, can_be_bought, image="GUI/images/property_cards/CS.png"):
        """ Creates an instance of the Tile object
            Should not be instantiated directly. """

        self._name = name
        self._position = position - 1
        self._can_be_bought = can_be_bought
        self._image = GUI.utils.rescale(pygame.image.load(image), 0.20)
        self._mortgaged = False
        #self._image2 = GUI.utils.grayscale(self._image)

    def get_name(self):
        """ Returns:
            The name of the Tile object as a string """
        return self._name

    def get_position(self):
        """ Returns:
            Intended position of the Tile within the Board as an integer. """
        return self._position

    def can_be_bought(self):
        """ Returns:
            True, if the Tile can be bought in-game, otherwise returns false. """
        return self._can_be_bought

    def get_image(self):
        """ Returns:
            The image for tile"""
        return self._image

    def get_image2(self):
        """Returns:
        The black and white image for the tile"""
        return self._image2

class ActionTile(Tile):
    """ A Monopoly game tile that triggers special interactions within the game.

        An ActionTile instance cannot be purchased by an agent within the game. Instead,
        instance specific actions will occur to players when this Tile is landed on.

        Attributes:
            position: An unique integer indicating its position within the Monopoly board
            name: A unique string of the tile's name
            TODO: add this to make it more speciifc
            action: An Action instance that provides output ....
            can_be_bought: A boolean that indicates whether this tile can be bought
    """

    def __init__(self, position, name, action, can_be_bought=False, image=None):

        """ Creates an instance of the ActionTile class

            Args:
                position: An unique integer indicating its position within the Monopoly board
                name: A unique string of the tile's name
                can_be_bought: A boolean that indicates whether this tile can be bought
                TODO: add this to make it more speciifc
                action: An Action instance that provides output ....

        """

        super().__init__(position, name, can_be_bought, image)

        self._action = action
        self._owner = Player("The Government", "")

    def get_action(self):
        """ Returns:
            The action for instance """
        pass


class PropertyTile(Tile):
    """ A tile in Monopoly that represents a single property

        A PropertyTile instance can be purchased by an agent within the game. If the property is developed within
        Monopoly, the rent of an instance of PropertyTile will increase depending on the amount of houses that a
        property has.

        Attributes:
            position: An unique integer indicating its position within the Monopoly board
            name: A unique string of the tile's name
            group: A string indicating the group of tiles this instance belongs to
            can_be_bought=True: A boolean that indicates whether this tile can be bought
            cost: An integer that indicates the amount of money that is required to purchase this property
            rent: An integer indicating the default, total amount of rent assigned to this property
            house_rent_1: An integer of the total amount of rent, if the property has 1 houses
            house_rent_2: An integer of the total amount of rent, if the property has 2 houses
            house_rent_3: An integer of the total amount of rent, if the property has 3 houses
            house_rent_4: An integer of the total amount of rent, if the property has 4 houses
            hotel_rent: An integer of the total amount of rent, if the property has a hotel
        """
    def __init__(self, position, name, group, cost, rent, house_rent_1, house_rent_2,
                 house_rent_3, house_rent_4, hotel_rent, can_be_bought=True, image=None, owner=None):

        """ Creates an instance of PropertyTile with the arguments assigned to the attributes of PropertyTile.

         Args:
             position: An integer indicating its position within the Monopoly board
            name: A string of the tile's name within PropertyTycoon
            group: A string indicating the group of tiles this instance belongs to
            can_be_bought=True: A boolean that indicates whether this tile can be bought
            cost: An integer that indicates the amount of money that is required to purchase this property
            rent: An integer indicating the default, total amount of rent assigned to this property
            house_rent_1: An integer of the total amount of rent, if the property has 1 houses
            house_rent_2: An integer of the total amount of rent, if the property has 2 houses
            house_rent_3: An integer of the total amount of rent, if the property has 3 houses
            house_rent_4: An integer of the total amount of rent, if the property has 4 houses
            hotel_rent: An integer of the total amount of rent, if the property has a hotel
            """

        super().__init__(position, name, can_be_bought, image)

        self._group = group
        self._cost = cost
        self._rent = rent
        self._house_rent = [house_rent_1, house_rent_2, house_rent_3, house_rent_4]
        self._hotel_rent = hotel_rent
        self._num_houses = 0
        self._num_hotel = 0
        self._owner = Player("The Bank", "The Bank")
        self._mortgaged  = False

    def get_house_count(self):
        """ Returns:
            An integer of the current amount of houses assigned to this property """
        return self._num_houses

    def get_hotel_count(self):
        """ Returns:
            An integer of the current amount of hotels assigned to this property"""
        return self._num_hotel

    def get_cost(self):
        """ Returns:
            The integer amount that this property costs"""
        return self._cost

    def add_house(self):
        """ Adds a house to the property. If there are 4 houses on this property, a house will not be added.

            Returns:
                A boolean indicating whether a house has been successfully added to the property.
                True, if there are less than 4 houses. False, otherwise.  """
        if self._num_houses != 4 and self._num_hotel == 0:
            self._num_houses += 1
            # print("You have purchased a house for " + self.get_name())
            return True
        else:
            # print("There are already 4 houses. You cannot add another house. Buy a hotel instead.")
            return False

    def add_hotel(self):
        """ Adds a hotel to the property. If there are less than 4 houses on this property, a hotel will not be added.
            If a hotel is already on this property, a hotel will not be added.

            Returns:
                A boolean indicating whether a hotel has been successfully added.
                True, if there 4 houses. False, otherwise.
        """
        if self._num_houses < 4:
            # print("You need 4 houses to purchase a hotel. Buy a house instead")
            return False

        elif self._num_hotel:
            # print("you already have a hotel, you cannot buy another")
            return False

        else:
            self._num_hotel = 1
            self._num_houses = 0
            # print("You have purchased a hotel for " + self.get_name())
            return False

    def demolish(self):
        """
        Demolish a hotel. If there is no hotel, demolish a single house. If there are no houses, do nothing.
        Returns:
            the refund price for building (int)
        """
        refund = 0
        if self._num_hotel == 1:
            self._num_hotel = 0
            self._num_houses = 4
            refund = self._cost
        else:
            if self._num_houses != 0:
                self._num_houses -= 1
                refund = self._cost
            else:
                refund = 0

        return refund

    def get_rent(self, game):
        """ Returns:
            The integer amount of rent that this property will incur, depending on the amount of houses or hotels
            purchased for this property. """
        current_player = game.get_turns().current()
        current_position = current_player.getPosition()
        current_tile = game.get_board().get_tile_at(current_position)
        owner = current_tile._owner


        if current_tile._group == 'Station':
                return current_tile.station_rent(owner)
        elif current_tile._group == 'Utilities':
                last_roll = game._last_roll
                return current_tile.utility_rent(owner, last_roll)
        else:
            if self.get_hotel_count():
                return self._hotel_rent
            elif self.get_house_count():
                return self._house_rent[self.get_house_count() - 1]
            else:
                if self.check_full_group(game):
                    return 2 * self._rent
                else:
                    return self._rent

    def station_rent(self, owner):
        "returns the rent for a station"
        num_stations = 0
        for t in owner.propertiesOwned:
            if t._name == "Brighton Station" or t._name == "Falmer Station" or t._name == "Hove Station" or t._name == "Lewes Station":
                num_stations += 1

        return [0,25,50,100,200][num_stations]


    def utility_rent(self, owner, last_roll):
        "returns the rent for a utility"
        num_utilities = 0
        for t in owner.propertiesOwned:
            if t._name == "Tesla Power Co" or t._name == "Edison Water":
                num_utilities += 1

        return last_roll * [0,4,10][num_utilities]

    def check_full_group(self, game):
        """
        Checks if the current player owns every tile belonging to this tile's group.
        """
        board = game.get_board()
        group_info = board.get_group_info()

        current_player = game.get_turns().current()

        tiles_in_the_group = board._group_info[self._group]

        all_clear = True

        for t in tiles_in_the_group:
            if t._owner != current_player:
                all_clear = False

        return all_clear


    def sell_to_bank(self, game):
        current_player = game.get_turns().current()
        if self._owner == current_player and self.get_house_count() == 0 and self.get_hotel_count() == 0:
            self._owner = Player("The Bank", "The Bank")
            current_player.getPropertiesOwned().remove(self)
            if self._mortgaged:
                prop_cost = int(self.get_cost() / 2)
                self._mortgaged = False
            else:
                prop_cost = self.get_cost()
            current_player.addBankBalance(prop_cost)

    def property_value(self):
        if self._mortgaged:
            return self._cost / 2
        else:
            return self._cost + self.get_house_count() * self._cost + self.get_hotel_count() * self._cost
