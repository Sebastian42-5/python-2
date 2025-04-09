class Point:
    
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


# Main program 

p1 = Point(2, 3)

print(f'({p1.x}, {p1.y})')


# you cannot put more than one constructor. It's always going to take the last one 