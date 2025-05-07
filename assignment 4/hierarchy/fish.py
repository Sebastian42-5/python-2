from animal import Animal

class Fish(Animal):

    def __init__(self, fins = 7):
        
        super().__init__(fins)

    def __repr__(self) -> str:
        return super().__repr__() + '\nClass: Fish'
    
    def reproduce(self) -> str:
        result = '\nFish reproduction varies largely. Some give birth to live young while others lay eggs.'
        return super().reproduce() + result
    
    def move(self):

        print('Fish move by swimming with their fins.')

    def sleep(self):

        print('Fish do not sleep a lot. They have to keep swimming.')
    

    
    
    