from progression import Progression

class GeometricSeries(Progression):
    def __init__(self, a = 1, r = 2, start = 1):
        super().__init__(start)
        self.start = start
        self.a = a
        self.r = r
    
    def reset(self):
        self._current = self.start
    
    def _advance(self):
        self._current += 1

    def __next__(self):
        if self._current is None:
            raise StopIteration 
  
        value = round((self.a * (self.r ** (self._current - 1))), 2)

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

    gs = GeometricSeries(2, 1.2)

    gs_lst = gs.lstProgression(10)


    for value in gs_lst:
        print(value)


    print(gs.gSum())

    print(gs_lst)

    gs.reset()

    print(gs.sumProgression(5))
    

# here, a reset was created bc once gseries is an iterator, not iterable. That means that it doesn't go back to the point. The self._current private 
# needs to be reseted to 0 for every usage. 