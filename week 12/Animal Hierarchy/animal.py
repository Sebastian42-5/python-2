from __future__ import annotations

class Animal:
    def __init__(self, legs = 0):
        '''create animal with legs'''
        self.legs = legs

    
    def walk(self) -> None:
        print(f'This animal walks with their {self.legs} legs')

    
    def sleep(self) -> None:
        print(f'DIfferent animals have different sleeping habits')

    
    def __repr__(self) -> None:
        return f'Animal I dont know number of legs: {self.legs}'

  

if __name__ == '__main__':

    anim = Animal(6)

    print(anim)

    print()

    anim.walk()

    anim.sleep()

    print()
