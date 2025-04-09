# Sebastian Soto 2432947


# function needed for part 2


def toCelsius(F):
    C =  round(((F - 32) * (5 / 9)), 2)
    return C 


# I forgot to put round in my function when I first submitted part 1


# function for part 2


def belowFreezing(temp_dict):
    freezing_temps = []
    for year in temp_dict:
        for temp in temp_dict[year]:
            if temp < 0:
                freezing_temps.append(temp)
    return freezing_temps



# Part 1 of main program (necessary for the rest to work)



input_file = open('data.txt', 'r')

interested_data = input_file.readlines()[4:]

temp_dict = {}

for line in interested_data:
    info = line.rstrip().split()

    key = info[0]

    data = list(map(toCelsius, list(map(float, info[1:]))))

    temp_dict[key] = data 




# part 2 of Main program


output_file = open('data_celsius.txt', 'w')

input_file.seek(0)

starter_info = input_file.readlines()[:4]


output_file.writelines(starter_info)


for year in temp_dict:

    str_for_year = list(map(str, temp_dict[year]))

    temperatures = '\t'.join(str_for_year)

    output_file.write(year + '\t' + temperatures)

    output_file.write('\n')


output_file.close()

input_file.close()
