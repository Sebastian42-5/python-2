from heterotroph import Heterotroph

class Carnivore(Heterotroph):

    def eat(self):
        super().eat()
        
        print('I eat animals')

    
    def __repr__(self):

        result = 'This organism is carnivore. Characterized by highly developed teeth,'

        return super().__repr__() + result




