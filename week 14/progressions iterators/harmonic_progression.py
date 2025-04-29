from progression import Progression
from lab11 import Fraction

class HarmonicProgression(Progression):
    
    def __init__(self, num = 1, denom = 1):
        super().__init__(Fraction(num, denom))
    
    def _advance(self):
        new_num = 1
        new_denom = self._current.denominator + 1
        self._current = Fraction(new_num, new_denom)


if __name__ == '__main__':
    hp = HarmonicProgression()

    for value in hp.lstProgression(10):
        print(value)

    # hp.printProgression(10)

    

        






        