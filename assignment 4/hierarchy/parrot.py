from omnivore import Omnivore 
from bird import Bird
from pet import Pet


class Parrot(Bird, Omnivore, Pet):
    def __init__(self, legs = 2, wings = 2):
        Pet.__init__(self, legs)
        Bird.__init__(self, wings)

    def __repr__(self) -> str:
        result = 'Species: Parrot'
        result = Bird.__repr__(self) + result
        result += '\n' + Pet.__repr__(self)
        return result + '\n' + Omnivore.__repr__(self)
    
    def reproduce(self) -> str:
        result = '''
Parrots often take a few days to lay a few clutch of eggs.
This can be as many as three to four eggs. 
    '''
        return super().reproduce() + result 
    
    def move(self):
        print('''I can move in various ways. I can fly, walk, climb and
even use an unique method called 'beakation' to traverse
narrow branches.''')
        
    def sleep(self):
        print('''Parrots sleep around 10 to 12 hours each night, often tucked under 
their wings. They might also take naps during the day.
              ''')
        
    def eat(self):
        Omnivore.eat(self)
        print('''
I eat both plant and animal matter. My natural diet include a variety 
of fruits like seeds, nuts, fruits, vegetables, flowers, buds and insects.  ''')


# some testing 

if __name__ == '__main__':
    p = Parrot()
  
    print(p.legs)
    print(p.wings)
    print(p)

    print()
    print(p.reproduce())

    print()
    p.sleep()

    print()
    p.move()

    print()
    p.eat()

    print()
    print(p.pet())



    
    