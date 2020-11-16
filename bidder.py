from GUI.utils import Button, GameText, InputBox, rescale
import pygame
import time
import random
class Bidder:
    def __init__(self, game):
        self._players = game._players
        self._num_players = len(self._players)
        self._max_bid = 0
        self._max_bid_player = self._players[0]
        self._current_player = self._players[0]
        self._game = game

    def bid(self):
        DISPLAY_SIZE = (400, 300)
        DISPLAY_COLOR = (255, 255, 255)
        gamedisplay = pygame.display.set_mode(DISPLAY_SIZE)
        pygame.display.set_caption("Bidding Screen")

        text_color = (30,30,30)
        title_string = "Bidding Screen: "
        title = GameText((3, 12), title_string, text_color, 32)

        instruction_text = self._current_player.getPlayerName() + ", Place your bid below: "
        instruction = GameText((5, 50), instruction_text, text_color, 22)
        # Button
        next_button = Button((170,230), "GUI/images/name_selection_images/button_next1.png", "GUI/images/name_selection_images/button_next2.png", "GUI/images/name_selection_images/button_next2.png", 1)
        # Background
        background = pygame.image.load("GUI/images/backgrounds/background9.png")

        box = InputBox(35, 120, 270, 40)

        intro = True
        while intro:
            for event in pygame.event.get():

                box.handle_event(event)

                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if next_button.over():
                        if box.text != "": #check numbers?
                            the_bid = int(box.text)
                            if the_bid > self._max_bid:
                                self._max_bid = the_bid
                                self._max_bid_player = self._current_player
                            else:
                                return "done"


            gamedisplay.blit(background, (-700, -250))

            box.draw(gamedisplay)
            title.show(gamedisplay)
            instruction.show(gamedisplay)
            next_button.show(gamedisplay)

            pygame.display.update()

    def ai_bid(self):
        DISPLAY_SIZE = (400, 300)
        DISPLAY_COLOR = (255, 255, 255)
        gamedisplay = pygame.display.set_mode(DISPLAY_SIZE)
        pygame.display.set_caption("Bidding Screen")

        text_color = (30,30,30)
        title_string = "Bidding Screen: "
        title = GameText((3, 12), title_string, text_color, 32)

        instruction_text = self._current_player.getPlayerName() + ", Place your bid below: "
        instruction = GameText((5, 50), instruction_text, text_color, 22)
        # Button
        next_button = Button((170,230), "GUI/images/name_selection_images/button_next1.png", "GUI/images/name_selection_images/button_next2.png", "GUI/images/name_selection_images/button_next2.png", 1)
        # Background
        background = pygame.image.load("GUI/images/backgrounds/background9.png")
        gamedisplay.blit(background, (-700, -250))
        box = InputBox(35, 120, 270, 40)
        box.draw(gamedisplay)
        title.show(gamedisplay)
        instruction.show(gamedisplay)
        next_button.show(gamedisplay)
        pygame.display.update()

        time.sleep(2)

        gamedisplay.blit(background, (-700, -250))
        title.show(gamedisplay)
        instruction.show(gamedisplay)
        next_button.show(gamedisplay)
        box.text = str(random.randint(40,350))
        box.box_render()
        box.draw(gamedisplay)

        #box.handle_event(event)
        the_bid = int(box.text)

        pygame.display.update()
        time.sleep(3)

        if the_bid > self._max_bid:
            self._max_bid = the_bid
            self._max_bid_player = self._current_player
        else:
            return "done"

    def fix_screen(self):
        self._game.get_board().setup_board()

    def bid_all(self):
        for current_player in self._players:
            self._current_player = current_player
            if self._current_player._ai:
                self.ai_bid()
            else:
                self.bid()

        self.fix_screen()

        max_bidder = self._max_bid_player
        max_bid = self._max_bid
        return max_bidder, max_bid
