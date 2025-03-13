'''

Every evening villahers on a small villahe gather around a big fire and sing sonhs

A promminent member of the comm is the bard every enening if the bard is present. he sings
a band new songs that no villager has heard before and no other song is sung that nught in the event
that the bard is not present, other villagers sings w out him exchange all siongs that they know (note:
all villagers cna only lean a new songs from the bard)

Given the list of villagers present for E consecutive evenings, output all villagers
that know all songs sung during that period

villagers start knowing 0 songs 

1 bard and villager 1 is a bard 


INPUT SPECIFICATION:

--> first line 

you may assume no villager will appear twice in one night and the bard will appear 


OUTPUT SPECIFICATION:

output all villagers that know all songs, including the bard, one integer per line in ascending order

Sample input 1-
4 (villagers)
3 (evenings)
2 1 2 (people, villagers (villager 1 is the bard, he knows an initial song)) (when villager 1 is there, there is a new song)
3 2 3 4 
3 4 2 1 


Sample Output 1-

1
2
4


Sample input 2-

8
5
4 1 3 5 4
2 5 6
3 6 7 8 
2 6 2
4 2 6 8 1

Sample output 2-

1
2
6
8

Sample input -3:

5 
3
2 1 3
2 2 1
4 2 1 4 5

Sample output -3:

1


'''

def bard():
    pass
