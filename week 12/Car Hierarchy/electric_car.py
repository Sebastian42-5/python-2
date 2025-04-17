from car import Car

class Battery:
    def __init__(self):
        self.battery = 40
    
    def __repr__(self):
        return f'The battery size is: {self.battery}'
    
    def changeBattery(self, new_battery):
        if new_battery > self.battery:
            self.battery = new_battery

    def mileage(self):
        m = (225 - 150) // (65 - 40)

        print(f'Your mileage is {self.battery * m}')

    

class ElectricCar(Car):
    def __init__(self, brand, model, year, battery: Battery):
        super.__init__(0)

        self.battery = battery 

    def __repr__(self):
        return f'brand: {self.brand[0].upper()}{self.brand[1:]} model: {self.model[0].upper()}{self.model[1:]} year: {self.year}'

    
    def gasTank(self):
        print('This car has no gaz tank')



my_car = ElectricCar('Toyota', 'Corolla', 2025, 20)


print(my_car.battery)

    

    








    

