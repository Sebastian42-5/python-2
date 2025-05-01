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
    
if __name__ == '__main__':
    print('Default Progression: ')
    Progression().printProgression(6)
    Progression(12).printProgression(11)

    for value in Progression().lstProgression(10):
        print(value*2)
    
    # for item in Progression(12):
    #     print(item)  # this is infinite

# protected constructors can be used outside the class constructuor, but not advisable _hey
# private constructors, you just can't use it in the main program __hey__. Only within the creation of the class