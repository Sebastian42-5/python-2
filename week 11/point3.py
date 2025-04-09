from __future__ import annotations

import math

class Point:
    
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def translate(self, dx: int, dy: int) -> None:
        ''' Move this Point dx horizontally and dy vertically'''
        self.x = self.x + dx
        self.y = self.y + dy 
    
    def distance(self, other_point: Point) -> float:
        '''return distance between this Point and other_point'''
        a = (other_point.x - self.x) ** 2
        b = (other_point.y - self.y) ** 2

        return math.sqrt(a + b)
    
    def __repr__(self) -> str:
        return f'({self.x}, {self.y})'
    

    def __lt__(self, other_point: Point) -> bool:
        '''return true if this Point and other_point are of 
        type Point and x, y of this Point is less and the x, y
        of other_point'''

        return isinstance(other_point, Point) and \
                self.x < other_point.x and \
                self.y < other_point.y
    

    def __eq__(self, other_point: Point) -> bool:
        '''return true if this Point and other_point are of 
        type Point and x, y of this Point is less and the x, y
        of other_point'''

        return isinstance(other_point, Point) and \
                self.x == other_point.x and \
                self.y == other_point.y
        



# __et__ < 

# __eq__ ==


# Main program 

p1 = Point(2, 3)

p2 = Point(5, 6)

print(p1)

print(p2)

# print(f'({p1.x}, {p1.y})')

p1.translate(3, 7)

# print(f'({p1.x}, {p1.y})')


print(p1.distance(p2))


# every constructor is defined by the __init__(): function 

p3 = Point(0,3)

p4 = Point(8, 3)


print('p3 <? p4: ', p3 < p4)

print('p3 ==? p4: ', p3 == p4)