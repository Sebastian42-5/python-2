def binarySearch(lst, low, high, target):
    if high >= low:
        mid = (high + low) // 2

        if lst[mid] == target:
            return mid
        
        elif lst[mid] > target: # search in left half
            return binarySearch(lst, low, mid - 1, target)
        
        else:
            return binarySearch(lst, mid + 1, high, target)
    
    else:
        return - 1
    


lst = [3, 5, 7, 8, 9, 10, 12, 14, 17, 19]

target = 17

low = 0

high = len(lst) - 1

result = binarySearch(lst, low, high, target)



if result != 1:
    print(f'Element {target} is present at index {result}')
else:
    print(f'Element {target} was not found in the list')

        
    


