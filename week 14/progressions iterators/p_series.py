from progression import Progression
from lab11 import Fraction

class Pseries(Progression):
    
    def __init__(self, num = 1, denom = 1, base = 1):
        super().__init__(Fraction(num, denom))
        self._p = base
        self._d = denom

    
    def _advance(self):
        self._d += 1
        new_num = 1
        new_denom = self._d ** self._p
        self._current = Fraction(new_num, 1) / Fraction(new_denom, 1)


if __name__ == '__main__':
    hp = Pseries(1, 3, 0.5)

    for value in hp.lstProgression(10):
        print(value)

    # hp.printProgression(10)

    
