'''

>>> output_file = open('hey.txt', 'w')
>>> word_lst = []
>>> for i in range(5):
...     line = input('enter data: ')
...     word_lst.append(line)
...
enter data: student grades
enter data: sigma
enter data: epsilon
enter data: weird
enter data: this is boring and therefore, you prefer coffee
>>> word_lst
['student grades', 'sigma', 'epsilon', 'weird', 'this is boring and therefore, you prefer coffee']
>>> output_file.writelines(word_lst)
>>> output_file.close()
>>> output_file = open('word.txt', 'r')

>>> input_file = open('word.txt', 'r')
>>> lst = input_file.readlines()
>>> lst
[]
>>> # you can read all lines from a file into a list
>>>



>>> lst_stripped = list(map(str.rstrip, lst2))
>>> lst_stripped
['item1', 'item2', 'item3']


'''