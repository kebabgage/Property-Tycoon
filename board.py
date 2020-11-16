import json
import pygame

import tile
import GUI
import die
import display_token
import display_tile
import buttons
import player_screen

class Board:

    def __init__(self):
        self._tile_list = []

    def populate_board(self):
        '''fills up the list of tiles'''
        with open("PropData.json", "r") as read_file:
            json_format = json.load(read_file)

        for item in json_format:
            self._tile_list.append(self.create_tile(item))

    def create_tile(self, json_tile):
        position = json_tile['Position']
        name = json_tile['Space/property']
        group = json_tile['Group']
        action = json_tile['Action']
        can_be_bought = json_tile['Can be bought?']
        cost = json_tile['Cost']
        rent = json_tile['Rent (unimproved)']
        rent1 = json_tile['1 house']
        rent2 = json_tile['2 houses']
        rent3 = json_tile['3 houses']
        rent4 = json_tile['4 houses']
        hotel = json_tile['1 hotel']
        image = json_tile['image']
        if can_be_bought:
            t = tile.PropertyTile(position, name, group, cost, rent, rent1, rent2, rent3, rent4, hotel, can_be_bought, image)
        else:
            t = tile.ActionTile(position, name, action, can_be_bought, image)
        return t

    def get_tile_list(self):
        return self._tile_list

    def get_tile_at(self, int):
        return self._tile_list[int]

    def get_display(self):
        return self._display

    def get_group_info(self):
        """
        Returns a dictionary Group -> list of tiles.
        Use this to access all tiles that belong to a certain group.
        """
        groups = dict()
        for t in self._tile_list:
            if type(t) == tile.PropertyTile:
                groups[t._group] = []
        for t in self._tile_list:
            if type(t) == tile.PropertyTile:
                groups[t._group].append(t)
        return groups

    def setup_board(self):
        """
        Called once before the game begins.
        Sets up the board, display and images to be used.
        """
        self.populate_board()

        # load images
        self._background = pygame.image.load("GUI/images/backgrounds/background2.jpg")
        self._board_image = pygame.image.load("GUI/images/board.jpg")

        # create display
        self._DISPLAY_SIZE = (1440,770)
        self._DISPLAY_COLOR = (110,110,110)
        self._display = pygame.display.set_mode(self._DISPLAY_SIZE)
        #self._display = pygame.display.set_mode(self._DISPLAY_SIZE, pygame.FULLSCREEN) # full screen
        pygame.display.set_caption("Property Tycoon")

        # create tile rects
        self._tile_rects = display_tile.create_tile_rects()
        self._group_info = self.get_group_info()

    def draw_board(self, game):
        """
        Draw these every frame.
        """
        self._display.fill(self._DISPLAY_COLOR)
        self._display.blit(self._background, (0, 0))
        self._display.blit(self._board_image, (0, 0))
        display_token.display_token(game)
        player_screen.display_player_screen(game)
        display_tile.display_current_tile(game)
        display_tile.display_target_tile(game)
        game._clock.display_time(game)
        buttons.button_concede.show(self._display)
