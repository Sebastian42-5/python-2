from animal import Animal

class Reptile(Animal):

    def __repr__(self):

        result = 'Class: Reptile'

        return super().__repr__() + result 
    
    def reproduce(self) -> str:
        result = '\nReptiles reproduce by laying eggs, typically on land rather than water.'
        
        return super().reproduce() + result
    
    def move(self):

        print('Reptiles normally move on the ground but can also swim.')

    def sleep(self):

        print('Reptiles sleep 4 to 7 hours each night.')
    