from instrument import Instrument

class StringInstrument(Instrument):
    def __repr__(self):
        return f'Instrument type: String \n Instrument name: {self.name}'
    
    def play_sound(self):
        print('vibration of strings')


    
    
    