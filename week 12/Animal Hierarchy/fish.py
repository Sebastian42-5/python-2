from __future__ import annotations

from animal import Animal

class Fish(Animal):
    def __init__(self, colour):
        # super().__init__(0)
        self.type = 'fish'
        self.colour = colour

    def walk(self) -> None:
        print('fish do not walk they swim')
    
    def sleep(self):
        print('Fish rest by reducing their activity and metabolism')

    
    def __repr__(self) -> str:
        return f'Animal: {self.type}\nColour: {self.colour}'
    

    def changeColour(self, colour) -> None:
        self.colour = colour

    def sameColour(self, other_fish: Fish) -> bool:
        return isinstance(other_fish, Fish) and self.colour == other_fish.colour



if __name__ == '__main__':
    fish = Fish('blue')

    print(fish)

    print()

    fish.walk()

    fish.sleep()

    fish.changeColour('black stripped')

    fish2 = Fish('blue')

    print(fish.sameColour(fish2))

