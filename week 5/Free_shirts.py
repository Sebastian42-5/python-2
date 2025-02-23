N, M, D = int(input()).split()

E = input().split

laun = 0

dirty = 0

for i in range(1, D + 1):
    if N == 0:
        laun += 1
        N = dirty 
        dirty = 0
    N += E.count(str(i)) - 1
    dirty += 1
    
print(laun)





