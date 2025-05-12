from abc import ABCMeta

class Vehicle(object, metaclass = ABCMeta):
    def __init__(self, brand, year = 2000):
        self.brand = brand 
        self.year = year 

        

    
