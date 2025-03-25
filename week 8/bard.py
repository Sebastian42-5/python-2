'''

Every evening villagers on a small villahe gather around a big fire and sing sonhs

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

only the bard sings 


'''

def bard():
    villagers = int(input('Enter the number of villagers: '))
    evenings = int(input('Enter the number of evenings: '))

    known_songs = {1: {1}}

    all_songs = set([1])

    for _ in range(evenings):
        evening = list(map(int, input('Enter the number of villagers followed by the number of each villager in the evening: ').split()))

        evening.pop(0)

        the_bard_is_present = 1 in evening

        if the_bard_is_present:
            new_song = max(all_songs) + 1
            all_songs.add(new_song)
            for villager in evening:
                if villager not in known_songs:
                    known_songs[villager] = set()
                known_songs[villager].add(new_song)
        
        else:
            shared_songs = set()
            for villager in evening:
                if villager in known_songs:
                    shared_songs.update(known_songs[villager])
            for villager in evening:
                if villager not in known_songs:
                    known_songs[villager] = set()
                known_songs[villager].update(shared_songs)
            all_songs.update(shared_songs)

    villagers_that_know_all_songs = sorted([villager for villager in known_songs if known_songs[villager] == all_songs]) 

    for villager in villagers_that_know_all_songs:
        print(villager)


bard()











    
