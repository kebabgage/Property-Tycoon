import random

class TurnManager:
    """
    A class to manage the order of turns amongst game players.
    """

    def __init__(self, players):
        """
        Construct a new turn manager based on game players.

        Parameters:
            players (List<T>): An ordered list of players to store.
        """
        self._players = players
        # Start in correct direction
        self._direction = True
        self._location = 0
        self._max = len(players)
        # True if the turn is still going in
        self._status = True
        self._go_again = False

    def current(self):
        return self._players[self._location]

    def next(self):
        self._go_again = False
        self._status = True
        return self.skip(count=0)

    def previous(self):
        self._go_again = False
        self._status = True
        self._location -= 1
        self._location %= self._max

    def get_player(self, position):
        return self._players[position]

    def status(self):
        return self._status

    def end_turn(self):
        self._status = False

    def go_again():
        self._status = True
        self._go_again = False

    def skip(self, count=0):
        count += 1
        self._location += count
        self._location %= self._max
        return self._players[self._location]

    def remove_current_player(self):
        self._players.pop(self._location)
        self._max -= 1
        if self._location == self._max:
            self._location -= 1

    def roll(self):
        roll1, roll2 = random.randint(1,6), random.randint(1,6)
        return roll1, roll2
