from __future__ import annotations
from car import Car
from battery import Battery


class ElectricCar(Car):
    def __init__(self, brand, model, year):
        super().__init__(brand, model, year)

        self.battery = Battery()
    
    def gasTank(self):
        print('This car has no gaz tank')


if __name__ == '__main__':

    my_car = ElectricCar('Toyota', 'Corolla', 2025)

    print(my_car)

    print(my_car.battery.mileage())

    

    








    

