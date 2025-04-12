# solution: 


def total_change(waiting_list, price): 

    money_change = set()

    for name in waiting_list:
        total_money = 0
        for bill, amount in waiting_list[name].items():
            total_money += bill * amount
        
        change = total_money % price

        money_paid = total_money - change

        money_change.add((name, money_paid))
    
    return money_change



def best_backyard(money_change):

    dimensions = set()

    for element in money_change:
        closest_pair = None
        smallest_diff = 9999
        area = element[1]
        for width in range(1, int(area ** 0.5) + 1):
            if area % width == 0:
                length = area // width
                diff = abs(length - width)

                if diff < smallest_diff:
                    smallest_diff = diff

                    closest_pair = (element[0], length, width)
        
        if closest_pair:
            dimensions.add(closest_pair)

    return dimensions


# main program 

waiting_list = {'Jessica': {5: 10, 10: 5, 20: 6, 50: 2, 100: 0}, 
 'Bob': {5: 5, 10: 8, 20: 7, 50: 1, 100: 1}, 
 'Kevin': {5: 2, 10: 5, 20: 4, 50: 3, 100: 2}, 
 'Lea': {5: 50, 10: 9, 20: 3, 50: 0, 100: 3} } 

price = 15

money_change = total_change(waiting_list, price)

dimensions = best_backyard(money_change)

print(money_change)

print(dimensions)


output_file = open('fences.txt', 'w') 


for person in dimensions:

    name, length, width = person

    output_file.write(name)

    output_file.write('\n')

    output_file.write(' ' + '_' * (length * 2) + '\n')

    for _ in range(width):
        output_file.write('|' + '  ' * length + '|\n')
    
    output_file.write(' ' + '_' * (length * 2) + '\n\n')

    output_file.write('\n')


output_file.close()
