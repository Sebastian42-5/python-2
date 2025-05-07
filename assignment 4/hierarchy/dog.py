from __future__ import annotations
from omnivore import Omnivore
from mammal import Mammal
from pet import Pet
from heterotroph import Heterotroph

class Dog(Mammal, Omnivore, Pet):

    def __init__(self, legs = 4, ears = 2, tail_length = 54, fangs = 4):
        Pet.__init__(self, legs)
        Heterotroph.__init__(self, legs=legs, fangs=fangs)
        self.ears = ears
        self.tail_length = tail_length

    
    def __repr__(self) -> str:
        result = '\nSpecies: Dog\n'
        result = Mammal.__repr__(self) + result
        result += '\n' + Pet.__repr__(self)
        result += '\n' + Omnivore.__repr__(self)
        return result
    
    def move(self):
        print('This animal likes to run and play around.')
        
    def sleep(self):
        print('Dogs sleep 12 to 14 hours every day. They are day creatures.')
        

    def eat(self):
        Omnivore.eat(self)
        print('I mostly eat dog food and I like chewing on bones.')

    def reproduce(self) -> str:
        result = 'Dogs do not reproduce that often'
        return Mammal.reproduce(self) + '\n' + result


# some testing   

if __name__ == '__main__':

    d = Dog()

    print(d)

    print()
    d.reproduce()

    print()
    d.sleep()

    print()
    d.move()

    print()
    d.eat()

    print()
    print(d.pet())

    print(d.fangs)

    print(d.tail_length)





        


    




