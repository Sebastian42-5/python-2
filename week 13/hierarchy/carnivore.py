from heterotroph import Heterotroph

class Carnivore(Heterotroph):

    def __init__(self, fangs = 4):
        
        self.fangs = fangs

    def eat(self):
        super().eat()
        
        print('I eat meat.')

    
    def __repr__(self) -> str:

        result = '''
        This organism is a carnivore. It feeds on other animals, 
        and its physical features facilitate hunting.
                '''

        return super().__repr__() + result




