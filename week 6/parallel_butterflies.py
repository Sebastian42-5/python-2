def new_sighting(kinds, counts, sighting):
    if sighting not in kinds:
        kinds.append(sighting)
        counts.append(0)

    i = kinds.index(sighting)

    counts[i] += 1
    


kinds = ['Monarch', 'Painted Lady', 'Bronze Copper', 'Orange Sulphur']

counts = [5, 2, 12, 7]

for i in range(len(kinds)):
    print(f'{kinds[i]}: {counts[i]}')

print()

new_sighting(kinds, counts, 'Common Blue')

for i in range(len(kinds)):
    print(f'{kinds[i]}: {counts[i]}')

print()



