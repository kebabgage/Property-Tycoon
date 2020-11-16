"""
Deck

Use get_decks() to initialize the decks
    deck_pot_luck, deck_opportunity_knocks = get_decks()

Use draw() to get the next card
    new_card = deck_pot_luck.draw()
"""

from card import Card
from random import shuffle
from copy import copy

class Deck:
    def __init__(self, card_list):

        self._cards = card_list
        self._cards_info = copy(card_list)

    def draw(self):
        """
        Returns a Card object.
        If there are no cards remaining in the deck, returns a dummy Card object that does nothing, with ID=99.
        """
        if len(self._cards) == 0:
            print("ran out of cards!")
            self.refill()

        return self._cards.pop()



    def get_card_at(self, index):
        return self._cards[index]


    def remaining_cards(self):
        """
        Returns the number of cards remaining in the deck.
        Simply returns the length of the list of Cards.
        """
        return len(self._cards)

    def shuffle(self):
        """
        Shuffles the deck.
        Uses python's list shuffle function to shuffle
        """
        return shuffle(self._cards)

    def refill(self):
        self._cards = copy(self._cards_info)
        self.shuffle()
