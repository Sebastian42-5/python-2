def divisors(n):
    div = []
    if n < 0:
        n = n*-1
    for i in range(1, n + 1):
        if n % i == 0:
            div.append(i)
            div.append(-i)
    return div 

print(divisors(int(input())))


'''
valid = False

while not valid:
    s = input('enter a password: ')
    valid = 

'''
