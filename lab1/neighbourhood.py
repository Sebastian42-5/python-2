def villages(int):
    village_number = 0
    village_road = []
    number_of_villages = int(input("How many villages?"))
    for i in range(number_of_villages):
        village_number += 1
        village_position = int(input(f"Enter the position of the village {village_number}"))
        village_road.append(village_position)
    village_road.sort()

    village_sizes = []

    for i in range(1, village_road-1):
        size = calNeigh(i, village_road)
        village_sizes.append(size)

    village_sizes.sort()

    print(village_sizes[0])

def calNeigh(index: int, village_road) -> float:

    for i in range(1, village_road -1):
        middle_right = (village_road[i + 1] - village_road[i]) / 2
        middle_left = (village_road[i] - village_road[i - 1]) / 2

        size = middle_right - middle_left 
        
        size.append(size)

        return size



    

    
