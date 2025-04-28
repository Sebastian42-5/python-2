from progression import Progression 

class ArithmeticProgression(Progression):
    '''create a new arithmetic progression'''
    def __init__(self, increment = 1, start = 0):
        super().__init__(start) 
        self.increment = increment 

    def _advance(self):
        '''update current value by adding the fixed increment'''
        self._current += self.increment

if __name__ == '__main__':
    print('Arithmetic progression with increment of 5: ')
    ArithmeticProgression(5).printProgression(10)
    ArithmeticProgression(5, 2).printProgression(10)

    for value in ArithmeticProgression(5, 3).lstProgression(10):
        print(value*2)


