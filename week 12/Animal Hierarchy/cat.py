from animal import Animal

class Cat(Animal):
    def __init__(self):
        super().__init__(4)  # you're calling the parent constructor with 4 legs
        self.type = 'cat'

    
    def sleep(self, hours = None) -> None:
        if hours == None:
            print('Cats sleep in warm and comfortable places')

        else:
            print(f'Cats cam sleep for {hours} hours daily')

    
    def __repr__(self) -> str:
        return f'Animal: {self.type}\n Legs: {self.legs}'



if __name__ == '__main__':

    cat = Cat()
        
    print(cat)

    print()

    cat.walk() 

    cat.sleep()

    cat.sleep(12)