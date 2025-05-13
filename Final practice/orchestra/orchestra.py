from __future__ import annotations

from abc import ABCMeta, abstractmethod

class Instrument(object, metaclass = ABCMeta):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def play_sound(self):
        pass


class StringInstrument(Instrument):
    def __repr__(self):
        return f'Instrument type: String \n Instrument name: {self.name}'
    
    def play_sound(self):
        print('vibration of strings')


class WoodwindInstrument(Instrument):
    def __repr__(self):
        return f'Instrument type: Woodwind \n Instrument name: {self.name}'
    
    def play_sound(self):
        print('Resonant breathy tones')




class Orchestra(StringInstrument, WoodwindInstrument):
    def __init__(self, instruments= None):
        if instruments:
            self.instruments = instruments
        else:
            self.instruments = []
    
    def add_instrument(self, instrument):
        self.instruments.append(instrument)

    def perform(self):
        sounds = []
        for instrument in self.instruments:
            if isinstance(instrument, Instrument):
                sounds.append(instrument.play_sound())
        
        return sounds
    

if __name__ == '__main__':
    violin = StringInstrument('Violin')

    flute = WoodwindInstrument('Flute')

    my_orc = Orchestra()

    my_orc.add_instrument(violin)

    my_orc.add_instrument(flute)

    my_orc.perform()

    

    


    

    
        
