from animal import Animal

class Amphibian(Animal):

    def __repr__(self) -> str:
        result = 'Class: Amphibian'
        return super().__repr__() + result
    
    def reproduce(self) -> str:
        result = 'Amphibians reproduce by laying soft eggs in the water'
        
        return super().reproduce() + result
   
    

    