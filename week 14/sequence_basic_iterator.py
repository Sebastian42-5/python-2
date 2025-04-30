class Sequence:
    def __init__(self, start, end):
        self.start_num = start 
        self.end_num = end

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.start_num > self.end_num:
            raise StopIteration
        else:
            self.start_num += 1
            return self.start_num - 1 
    
    def __len__(self):
        return self.end_num - self.start_num + 1


if __name__ == '__main__':
    start, end = 3, 10

    seq = Sequence(start, end)

    print(len(seq))

    for elem in seq: 
        print('counting: ', elem)

    # for i in range(len(Sequence(3, 10))):
    #     print(f'i = {i}')

    print(len(seq))

    for elem in Sequence(3, 10):  
        print(elem)

# the pointer of the iterator goes to the beginning
    


