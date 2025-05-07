from animal import Animal

class Bird(Animal):

    def __init__(self, wings = 2):
        super().__init__(wings)

    def __repr__(self) -> str:
        return super().__repr__() + '\nClass: Bird\n'
    
    def reproduce(self):
        result = '''
Birds typically reproduce by hatching and incubating their eggs.
    '''
        return super().reproduce() + result 
    
    


