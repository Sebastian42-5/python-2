# 1

# output_file = open('apricots.txt', 'w')

# output_file.write('apricots are the\n')

# output_file.write('greatest of all fruits')

# output_file.close()



# txt_file = open('apricots.txt', 'r')


# txt_file.seek(0)

# line = txt_file.readline()

# while line != '':
#     print(line.rstrip())
#     line = txt_file.readline()

# txt_file.close()


# 2

# phrase = 'Hello World'

# count = 0 

# for char in phrase:
#     if char == 'a':
#         count += 1

# while True:
#     try:
#         num = int(input('>'))

#     except ValueError:
#         print('input causes a value error')

#     else:
#         print(num * len(phrase))
#         break



# 4


# from __future__ import annotations 

# class Menu:
#     def __init__(self):
#         self.options = []

#     def addOption(self, option: str) -> None:
#         self.options.append(option)

#     def getInput(self) -> str:

#         for i in range(len(self.options)):
#             print(f'{i + 1}) {self.options[i]}')

#         done = False

#         while not done:

#             try:
#                 choice_number = int(input('Enter the number of your choice: '))
#                 choice = self.options[choice_number - 1]

#             except ValueError:
#                 print('Input must be an integer')
            
#             except IndexError:
#                 print('Item number must be on the menu')


#             else:
#                 return choice



# my_menu = Menu()

# my_menu.addOption('Drink')

# my_menu.addOption('Side dish')

# my_menu.addOption('Main dish')

# my_menu.addOption('Dessert')

# my_menu.addOption('Quit')


# done = False

# while not done:
#     choice = my_menu.getInput()

#     print(f'choice: {choice}')

#     if choice == 'Quit':
#         done = True

