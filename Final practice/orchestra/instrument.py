from abc import ABCMeta, abstractmethod

class Instrument:
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def play_sound(self):
        pass

    