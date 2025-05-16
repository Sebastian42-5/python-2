from progression import Progression


class FibonacciProgression(Progression):
    def __init__(self, first = 0, second = 1):
        super().__init__(first)
        
        self._prev = second - first # value preceding first

    def _advance(self):
        temp = self._current 
        self._current += self._prev

        self._prev = temp 


if __name__ == '__main__':
    # FibonacciProgression().printProgression(10)

    for value in FibonacciProgression().lstProgression(10):
        print(value)



# finish this for Wednesday 

# also, create fib_iterable 


        

    