from vehicle import Vehicle

class Car(Vehicle):
    def __init__(self, brand, year, seats):
        super().__init__(brand, year)

        self.seats = seats

    def __repr__(self):
        return f'{self.brand} {self.year} {self.seats}'
    


if __name__ == '__main__':
    c = Car()

    print(c)

    