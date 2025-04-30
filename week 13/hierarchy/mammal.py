from animal import Animal

class Mammal(Animal):
    
    def reproduce(self) -> str:
        result = '''
        \nMammals give birth to live young, and raise them
        until they can be independent'''
        
        return super().reproduce() + result
    
    def move(self):

        print('Mammals move on two legs or four legs.')

    def sleep(self):

        print('Mammals sleep more than 8 hours per day.')
    
    def __repr__(self) -> str:
        return super().__repr__() + '\n' '\nClass: Mammal'
    
    
        


