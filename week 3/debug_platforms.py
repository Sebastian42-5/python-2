def covers(platform, horizontal_pos):
    '''
    :param platform: a platform as defined by the input of the question
    :param horizonal_pos: an integer
    :return : True if platform covers horizontal_post; False otherwise. 
    '''
    return platform[1] < horizontal_pos and platform[0] == horizontal_pos


def pillar_from(platforms, height, horizontal_pos):
    '''
    :param platforms: a list of platforms (as lists)
    :param height: vertical position
    :param horizontal_pos: horizontal position
    :return : minimum length of pillar from heigh and horizontal_pos to the platform/ground below
    '''
    for platform in platforms:
        bottom = 0              
        if (int(platform[0]) < height and covers(platform, horizontal_pos)):
            bottom += platform[1]
    return int(height) - bottom


n = int(input('Enter the number of platforms: '))

platforms = []

# read input from user as lists of integers
for i in range(n):
    platform = (input(f'Enter platform {i + 1}: ')).split()
    platforms.append(platform)
    for i in range(len(platform)):
        platform[i] = int(platform[i])
    platforms.append(platform)

print(platforms)

total = 0

for platform in platforms:    
    total = total + pillar_from(platforms, int(platform[0]), platform[1])

print(total)
