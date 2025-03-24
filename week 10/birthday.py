def birthday(n):
    birthdays = {}

    for i in range(n):
        firstname, month, day = input().split()

        day = int(day)

        pair = (month, day)

        if pair not in birthdays:

            birthdays[pair] = [firstname]
        else:
            birthdays[pair].append(firstname)
    
    # this works thanks to referencing 

    return birthdays


print(birthday(4))

        
