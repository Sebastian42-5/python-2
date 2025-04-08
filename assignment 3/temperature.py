# Sebastian Soto 2432947


# part 1 functions


def toCelsius(F):
    C =  round(((F - 32) * (5 / 9)), 2)
    return C

# Here, I forgot to put round when I first submitted part 1 


def avgTempYear(temp_dict, year):
    try:
        year_temps = temp_dict[year]
    except KeyError:
        print('The given year is not in the dictionary')
        return None

    else:
        temp_avg = round((sum(year_temps) / len(year_temps)), 2)

        return temp_avg



def topThreeYears(temp_dict):

    averages = set()

    three_biggest_lst = []

    max_avg = 0

    for year in temp_dict:
        avg = avgTempYear(temp_dict, year)
        averages.add(avg)

    for val in range(3):
        val = max(averages)
        averages.discard(val)
        three_biggest_lst.append(val)
    
    return three_biggest_lst



def avgTempMonth(temp_dict, month):

    month_dict = {'JAN': 1, 'FEB': 2, 'MAR': 3, 'APR': 4, 'MAY': 5, 'JUN': 6, \
                  'JUL': 7, 'AUG': 8, 'SEP': 9, 'OCT': 10, 'NOV': 11, 'DEC': 12}
    
    total_temp = 0

    for year in temp_dict:
        total_temp += temp_dict[year][month_dict[month] - 1]

    avg_for_month = round((total_temp / len(temp_dict)), 2)

    return avg_for_month


# part 2 functions (put inside part 1 for testing)


def belowFreezing(temp_dict):
    freezing_temps = []
    for year in temp_dict:
        for temp in temp_dict[year]:
            if temp < 0:
                freezing_temps.append(round(temp, 2))
    return freezing_temps



# Main program


input_file = open('data.txt', 'r')

interested_data = input_file.readlines()[4:]

temp_dict = {}

for line in interested_data:
    info = line.rstrip().split()

    key = info[0]

    data = list(map(toCelsius, list(map(float, info[1:]))))

    temp_dict[key] = data 



# part 2 main program (put inside part 1 for testing)


output_file = open('data_celsius.txt', 'w')

input_file.seek(0)

starter_info = input_file.readlines()[:4]


output_file.writelines(starter_info)


for year in temp_dict:

    str_for_year = list(map(str, temp_dict[year]))

    temperatures = '    '.join(str_for_year)

    output_file.write(year + '    ' + temperatures)

    output_file.write('\n')


output_file.close()

input_file.close()





# Some testing:





# year = '1972'
# temp_avg = avgTempYear(temp_dict, year)

# print(temp_avg)



# three_biggest = topThreeYears(temp_dict)

# print(three_biggest)


# month = 'JUL'

# avg_for_month = avgTempMonth(temp_dict, month)


# print(avg_for_month)


# freezing_temperatures = belowFreezing(temp_dict)


# print(freezing_temperatures)







