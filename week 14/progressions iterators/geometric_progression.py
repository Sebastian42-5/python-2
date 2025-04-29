from progression import Progression

class GeometricProgression(Progression):
    def __init__(self, base = 2, start = 1):
        super().__init__(start)
        self.base = base
    
    def _advance(self):
        self._current *= self.base 

if __name__ == '__main__':
    GeometricProgression(3).printProgression(10)


    for value in GeometricProgression(3).lstProgression(10):
        print(value)
    

