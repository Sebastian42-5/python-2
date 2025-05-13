from instrument import Instrument

class WoodwindInstrument(Instrument):
    def __repr__(self):
        return f'Instrument type: Woodwind \n Instrument name: {self.name}'
    
    def play_sound(self):
        print('Resonant breathy tones')

