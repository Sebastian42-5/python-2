class Battery:
    def __init__(self, battery_size = 40):
        self.battery = battery_size
    
    def describeBattery(self):
        return f'This car has a {self.battery}-Kwh battery'
    
    def changeBattery(self, new_battery):
        if new_battery > self.battery:
            self.battery = new_battery

    def mileage(self):
        m = (225 - 150) // (65 - 40)

        print(f'Your mileage is {self.battery * m}')