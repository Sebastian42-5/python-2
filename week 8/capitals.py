def capitals(d : dict):
    if 'Madagascar' not in d:
        d['Madagascar'] = 'Antananarivo'

    print(list(d.keys()), d)


# capitals({'Thailand': 'Bangkok', 'Malaysia': 'Kuala Lumpur'})



def isPerfect(n:int) -> bool:
    
    div = []

    for i in range(1, n + 1):
        if n % i == 0 and i != n:
            div.append(i)

    return sum(div) == n 


print(isPerfect(6))