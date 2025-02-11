'''What prints?'''

def numLoop():
    x = -5
    while x > -7:
        if x == -1:
            x = 50
            return x
    print(x)
    x = x + 1
    return 30

numLoop()

# This is an infinite loop, because x never gets reassigned, so x is never -1. That means that the while loop will keep checking if -5 is -1, since -5 > -7. 