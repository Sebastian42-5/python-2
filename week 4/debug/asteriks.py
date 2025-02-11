size = int(input('Select your triangle size: '))


for i in range(2):
    for i in range(size - 1, 0, -1):
        print('*' * (i + 1))
    for i in range(size - 1):
        print('*' * (i + 1))

