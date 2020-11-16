import time
import pygame
import GUI
import datetime

class Clock:
        def __init__(self):
                self._start_time = time.time()

        def set_time_limit(self, time_limit):
                self._time_limit = time_limit

        def get_game_time(self):
                diff = time.time() - self._start_time
                return diff

        def get_game_time_string(self):
                diff = self.get_game_time()
                return str(datetime.timedelta(seconds=diff))[0:7]

        def reset(self):
                self._start_time = time.time()

        def display_time(self, game):
                display = game.get_board().get_display()
                time_string = self.get_game_time_string()
                time_text = GUI.GameText((20,700), time_string, (40,40,40), 34)
                time_text.show(display)

        def abridged_check(self, game):
                return self.get_game_time_string() > self._time_limit


#c1 = Clock()
#print(c1.get_game_time())
#time.sleep(2)
#print(c1.get_game_time(), c1.get_game_time_string())

#print("0:01:00" > "0:00:59")
