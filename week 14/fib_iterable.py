class FibonacciIterable:
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        return FibonacciIterator(self.n)


class FibonacciIterator:
    def __init__(self, n):
        self._n = n 
        
        self._count = 0

        self._first = 0
        self._second = 1
    
    def __iter__(self):
        return self

    def __next__(self):

        if self._count >= self._n:
            raise StopIteration
        
        if self._count == 0:
            result = 0
        elif self._count == 1:
            result = 1
        else:
            result = self._first + self._second

            self._first, self._second = self._second, result


        self._count += 1

        return result


if __name__ == '__main__':
    my_fib = FibonacciIterator(10)
    for elem in my_fib:
        print(elem)
    for elem in my_fib:
        print(elem)

    