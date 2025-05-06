from abc import ABCMeta, abstractmethod

@abstractmethod
class Heterotroph(object, metaclass = ABCMeta):
    def __init__(self, legs = 0, fins = 0, fangs = 0, teeth = 0):
        self.legs = legs
        self.fins = fins
        self.fangs = fangs
        self.teeth = teeth

    def eat(self):
        print('I eat other organisms instead of generating my own food')

    
    def __repr__(self) -> str:
        return '''
This organism is a heterotroph. It is
unable to produce its own food, so it
eats other organisms. '''
    
    

