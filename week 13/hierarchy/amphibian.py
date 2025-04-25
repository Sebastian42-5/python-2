from animal import Animal

class Amphibian(Animal):

    def __repr__(self):

        result = 'Class: Amphibian'

        return super().__repr__() + result
    
    def reproduce(self) -> str:
        result = '\nAmphibians reproduce by laying soft eggs in the water'
        
        return super().reproduce() + result
    
    def move(self):

        print('Fish can swim but can also jump on the ground.')

    def sleep(self):

        print('Amphibians sleep more than 10 hours a day.')
    

    