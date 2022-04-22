from colorama import Fore, Back, Style, init
from datetime import datetime
from time import sleep
from my_func import countdown

init(autoreset=True)


class TrafficLight:
    __color = 'Цвет.. приватный цвет'

    def __init__(self):
        self.col = None
        self.slp = None

    def running(self, text_c, sleep_tl=True):
        self.col = text_c
        self.slp = sleep_tl
        color_list = [Fore.RED, Fore.YELLOW, Fore.GREEN]
        sleep_list = [7, 2, 5]
        for self.col, self.slp in zip(color_list, sleep_list):
            datetime.now()
            print(self.col + text_c)
            countdown(self.slp)
            # sleep(self.slp) #2 вариант


a = TrafficLight()
a.running('●')
print(a.col)
