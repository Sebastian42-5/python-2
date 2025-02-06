# jupyterhub.dawsoncollege.qc.ca
def isPrime(num):
    # 1 is not a prime number
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        # if the number is a composite, returns false
        if num % i == 0:
            return False
    return True

number = int(input('Enter a number: '))
number_list = list(range(2, number + 1))
prime_numbers = [num for num in number_list if isPrime(num)]

print(prime_numbers)


# print(isPrime(int(input('Enter a number: '))))

# primes = []

# n = 2

# while len(primes) < 100:
    # if isprimes(n):
    #   primes.append(n)
    # n += 1
    # print(primes)





    

    
        


                




