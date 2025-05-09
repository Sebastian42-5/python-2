from progression import Progression

class GeometricProgression(Progression):
    def __init__(self, a = 1, r = 2, start = 1):
        super().__init__(start)
        self.a = a
        self.r = r
    
    def _advance(self):
        self._current += 1

    def __next__(self):
        if self._current is None:
            raise StopIteration 
  
        value = self.a * (self.r ** (self._current - 1))

        self._advance()

        return value
    
    def gSum(self):
        if self.r < 1:
            sum = self.a / 1 - self.r

            return sum 
        
        else:
            return 'Divergent'


if __name__ == '__main__':
    # GeometricProgression(3).printProgression(10)

    gs = GeometricProgression(2, 1.2)


    for value in gs.lstProgression(10):
        print(value)


    print(gs.gSum())
    
