from progression import Progression


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

    def __repr__(self):
        return f'{self._num} / {self._d}^{self._p}'

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

    # hp.printProgression(10)

    
