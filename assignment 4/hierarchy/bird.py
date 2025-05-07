from animal import Animal

class Bird(Animal):

    def __init__(self, wings = 2, legs = 2):
        self.wings = wings
        super().__init__(legs)

    def __repr__(self) -> str:
        return super().__repr__() + '\nClass: Bird\n'
    
    def reproduce(self):
        result = '''
Birds typically reproduce by hatching and incubating their eggs.
    '''
        return super().reproduce() + result 
    
    


