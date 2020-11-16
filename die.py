from random import randrange
import pygame


class Die:

    #initializes first roll to [1,1]
    def __init__(self):
        self.numberRolls = [1,1]
        self.double_counter = 0

    #randomly selects two numbers between 1-6 to simulate two die rolling and returns the number
    def roll(self):
        self.numberRolls[0] = randrange(1,6,1)
        self.numberRolls[1] = randrange(1,6,1)

        if self.numberRolls[0] == self.numberRolls[1]:
            self.double_counter += 1

        return self.numberRolls
