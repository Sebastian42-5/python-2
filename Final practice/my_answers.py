class Progression:
    '''iterator producing a generic progression
    
    default iterator: 0, 1, 2, 3, ...'''

    def __init__(self, start = 0):
        self._current = start 

    def _advance(self):
        '''update self._current to a new value
        this should be overridden by a subclass to customize
        progression'''
        self._current += 1
    
    def __iter__(self):
        '''by convention, an iterator must return itself as an iterator'''
        return self
    
    def __next__(self):
        '''return the next element or else raise StopIteration error'''
        if self._current is None: # our convention to stop a progression 
            raise StopIteration
        else:
            answer = self._current
            self._advance()
            return answer
    
    def printProgression(self, n): # n represents the number of values that are printed
        '''print next n values of the progression'''
        print('  '.join(str(next(self)) for j in range(n)))
    
    def lstProgression(self, n):
        lst = [next(self) for _ in range(n)]
        return lst


# solution portion:



# g-series:


class GeometricSeries(Progression):
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

    gs = GeometricSeries(2, 1.2)


    for value in gs.lstProgression(10):
        print(value)


    print(gs.gSum())



# p-series:



class PseriesTerms:
    def __init__(self, num, denom, base):
        self.num = num 
        self.denom = denom 
        self.base = base
    
    def __repr__(self):
        return f'{self.num} / {self.denom}^{self.base}'
    

class Pseries(Progression):
    
    def __init__(self, num = 1, denom = 1, base = 1):
        super().__init__(PseriesTerms(num, denom, base))
        self._num = num
        self._p = base
        self._d = denom

    def _advance(self):
        self._d += 1
        self._current = PseriesTerms(self._num, self._d, self._p)

    def isConvergent(self):
        if self._p > 1:
            return 'Convergent'
        else:
            return 'Divergent'


if __name__ == '__main__':
    hp = Pseries(1, 2, 4)

    for value in hp.lstProgression(10):
        print(value)
    
    print(hp.isConvergent())





