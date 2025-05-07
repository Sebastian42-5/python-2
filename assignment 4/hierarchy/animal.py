from abc import ABCMeta, abstractmethod

class Animal(object, metaclass = ABCMeta):
    # abstract class
    def __init__(self, legs = 0, fins = 0):
        self.legs = legs
        self.fins = fins 
    
    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def sleep(self):
        pass

    @abstractmethod
    def eat(self):
        pass

    def reproduce(self) -> str:
        return 'Members of this kingdom reproduce by finding a mate of the same species'
    
    def __repr__(self) -> str:
        return 'Kingdom: Animalia'
    


