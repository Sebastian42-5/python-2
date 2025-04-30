from __future__ import annotations
from pet import Pet
from mammal import Mammal
from herbivore import Herbivore

class Bunny(Mammal, Herbivore, Pet): # the order of the parents is important
    def __init__(self, legs = 4, ears = 2):
        super().__init__(legs)
        # Mammal.__init__(self, legs) is preferred if the inheritance is more complicated

        self.ears = ears

    def __repr__(self) -> str:
        result = 'Species: Bunny'

        result = Mammal.__repr__(self) + result # kingdom, class

        result += '\n' + Pet.__repr__(self)

        return result + '\n' + Herbivore.__repr__(self)
    
    def reproduce(self):
        result = '''
        Bunnies can produce multiple litters per
        year, potentially having 3-8 kits per litter'''
        
        return super().reproduce() + '\n' + result

    def move(self):

        print('I move by hopping and I can see behind me...')

    
    def sleep(self):

        print('''
              Bunnies as nocturnal animals, typically
              sleep around 12 to 14 hours a day in short,
              intermittent periods.''')
        
    def eat(self):
        Herbivore.eat(self)
        print('''
            I mostly eat fresh hay and grass, with
            some leafy greens and few pellets. I should only
            be given fruit and root vegetables like carrots, as an occasional treat''')
        
    
if __name__ == '__main__':

    b1 = Bunny()
    #print(b1.legs)
    #print(b1.ears)
    print(b1)

    print()
    b1.reproduce()

    print()
    b1.sleep()

    print()
    b1.move()

    print()
    b1.eat()

    print()
    print(b1.pet())

    


        





    
