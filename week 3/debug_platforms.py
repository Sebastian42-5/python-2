def covers(platform, horizontal_pos):
    '''
    :param platform: a platform as defined by the input of the question
    :param horizonal_pos: an integer
    :return : True if platform covers horizontal_post; False otherwise. 
    '''
    left, right = platform[1], platform[2]

    return left <= horizontal_pos <= right


def pillar_from(platforms, height, horizontal_pos):
    '''
    :param platforms: a list of platforms (as lists)
    :param height: vertical position
    :param horizontal_pos: horizontal position
    :return : minimum length of pillar from heigh and horizontal_pos to the platform/ground below
    '''
    bottom = 0

    for platform in platforms:
        platform_height = platform[0]          
        if platform_height < height and covers(platform, horizontal_pos):
            bottom = max(bottom, platform_height)
    return height - bottom


n = int(input('Enter the number of platforms: '))

platforms = []

# read input from user as lists of integers
for i in range(n):
    platform = list(map(int, input(f'Enter platform {i + 1}: ').split()))
    platforms.append(platform)

print(platforms)

total = (pillar_from(platforms, platform[0], platform[1]) for platform in platforms)

print(total)
