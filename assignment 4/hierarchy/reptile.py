from animal import Animal

class Reptile(Animal):

    def __repr__(self) -> str:

        result = 'Class: Reptile'

        return super().__repr__() + result 
    
    def reproduce(self) -> str:
        result = 'Reptiles reproduce by laying eggs, typically on land rather than water.'
        
        return super().reproduce() + result
    