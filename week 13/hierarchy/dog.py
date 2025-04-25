from __future__ import annotations
from omnivore import Omnivore
from mammal import Mammal
from pet import Pet

class Dog(Mammal, Omnivore, Pet):

    def __init__(self, legs = 4, ears = 2):

        super().__init__(legs)
        self.ears = ears

    
    def __repr__(self):
        result = 'Species: Dog'

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

    def reproduce(self):
        result = 'Dogs do not reproduce that often'

        return Mammal.reproduce(self) + '\n' + result
        

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





        


    




