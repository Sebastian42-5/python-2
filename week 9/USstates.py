'''
Consider cities and states in the US. Each state is given a two letter abbreviation. You are tasked to read n cities and
d states from the user and determine the number of special pairs.

Here is an example of a special pair:
SCRANTON PA and PARKER SC.
This is special pair since the first two characters of each city gives the abbreviation for the other city's state. 
That is, SC PA and PA SC. 

A pair of cities is special if they meet this property and are not in the same state. Your task is 
to determine the number of special pairs of cities in the provided input. Make sure your code is efficient. That is, make use
of efficient data structures.

INPUT SPECIFICATION:

--> first line is an interger n 
--> next n lines: one per city. Each line gives the name of a city in uppercase, a space and it's state 
abbreviation in uppercase. note that the city name can exist in multiple states but will not appear more than once
in the same state.

OUTPUT SPECIFICATION:

output the number of special pairs of cities

SAMPLE INPUT:

12
SCRANTON PA
MANISTEE MI
NASHUA MH
PARKER SC
LAFAYETTE CO
WAHOUGAL WA
MIDDLEBOROUGH MA
MADISON MI
MILFORD MA
MIDDLETON MA
COVINGTON LA
LAKEWOOD CO

SAMPLE OUTPUT:

9 

SC PA (1)
MA MI (2) (3) (4)
NA NH
PA SC (1)
LA CO (5) 
WA WA
MI MA (2) (7)
MA MI (7) (8) (9)
MI MA (3) (8)
MI MA (4) (9)
CO LA (5) (6)
LA CO (6)


Read 5 different sample inputs from the user and write this to a file, where there is an empty line 
between any two sample inputs. 


'''

def special_pair(n, city_state):

    total_pairs = 0
    
    values = []

    d = {}

    for i in range(n):

        city, state = city_state.split()

        split_city = city[:2]

        d[i] = set([split_city, state])
    

    for j in range(len(d)):
        for k in range(len(d)):
            if d[j] == d[k]:
                total_pairs += 1

    return total_pairs


for _ in range(5):
    output_file = open('city_states.txt', 'w')

    n = int(input('Enter the number of cities: '))

    for i in range(n):

        city_state = input(f'Enter the city and the state for city {i + 1}: ')

        output_file.write(city_state)

        output_file.write('\n')

        print(special_pair(n, city_state))


output_file.close()
        










        
















