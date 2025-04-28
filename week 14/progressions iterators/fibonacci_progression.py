from progression import Progression 

class FibonacciProgression(Progression):
    def __init__(self, first = 0, second = 1):
        super().__init__(first)
        
        self._prev = second - first # value preceding first

    def _advance(self):
        self._current = self._prev 

if __name__ == '__main__':
    FibonacciProgression().printProgression(10)


# finish this for Wednesday 

# also, create fib_iterable 


        

    