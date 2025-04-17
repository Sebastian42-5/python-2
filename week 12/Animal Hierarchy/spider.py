from animal import Animal 

class Spider(Animal):
    def __init__(self):
        super().__init__(8)
        self.type = 'spider'

    def sleep(self) -> None:
        print('Spiders hibernate in their webs')


spider = Spider()
print(spider)