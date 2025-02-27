d = {}

d = {'Monarch': 5, 'Common Blue': 12}

# if 'starling' in d:
#     print('in the dictionary')
# else:
#     print('not in the dictionary')

# print(d['Monarch'])

# print(d['Hello'])

# print(d.get('starling'))

# print(d.get('Monarch'))

# print(len(d))

# d2 = d.clear()

# print(d2)

d = {'Monarch': 5, 'Common Blue': 12}

d['Painted Lady'] = 3

print(d)

a = d.pop('Painted Lady')

# print(a)

# print(d)

# del d['Monarch']

# print(d)

# keys in dictionaries are immutables
# values can be mutable or immutable 

# the keys have to be distinct

list_keys = list(d.keys())

print(list_keys)

# .items() gives a tuple

# pair in list(butterflies.times())


d.update(Monarch = 12)

print(d)

d.update(Bronze = 1)

print(d)

