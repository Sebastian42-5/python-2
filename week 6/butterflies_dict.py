def new_sighting(butterflies, sighting):
    butterflies[sighting] = butterflies.get(sighting, 0) + 1
    pass


butterflies = {'Monarch': 5, 'Painted Lady': 2, 'Bronze Copper': 12, 'Orange Sulphur': 7}


for key in butterflies:
    print(f'{key} : {butterflies[key]}')
print()

print(new_sighting(butterflies))






# kinds = ['Monarch', 'Painted Lady', 'Bronze Copper', 'Orange Sulphur']

# counts = [5, 2, 12, 7]
