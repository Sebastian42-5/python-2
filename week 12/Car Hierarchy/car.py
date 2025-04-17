from __future__ import annotations

class Car:
    def __init__(self, brand, model, year, odometer_reading = 0):
        self.brand = brand
        self.model = model
        self.year = year
        self.odometer_reading = odometer_reading
    
    def __repr__(self):
        return f'brand: {self.brand[0]}{self.brand[1:]} model: {self.model[0].upper()}{self.model[1:]}\
        year: {self.year} odometer: {self.odometer_reading}'
    
    def readOdometer(self):
        print(f'This car has {self.odometer_reading} miles on it')
    
    def update(self, new_miles):
        self.odometer_reading += new_miles

    def overwriting(self, mileage: int):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print('cannot roll back an odometer')



