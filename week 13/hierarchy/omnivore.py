from heterotroph import Heterotroph

class Omnivore(Heterotroph):
    def eat(self):
        super().eat()
        print('I eat anything!')
    
    def __repr__(self):
        result = 'This organism is an omnivore; it can eat feed on both plants and animals.'

        return super.__repr__() + result


