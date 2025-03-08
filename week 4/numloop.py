def numLoop():
    x = -5
    while x > -7:
        if x == -1:
            x = 50
            return x
        # else:
        #     x += 1
    print(x)
    x = x + 1
    return 30

numLoop()


# this is an infinite loop, because you are never changing the value of x inside of the while loop. If we trace this code, it's gonna look something like this:

# -5 > -7: infinite while loop 