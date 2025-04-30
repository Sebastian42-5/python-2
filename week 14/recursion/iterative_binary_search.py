# time complexity: O(log(n))
# space complexity:O(1)

# we assume that the list is sorted.

def binarySearch(lst, target):

    nums = lst

    l = 0
    m = 0 
    r = len(nums) - 1


    while l <= r: # if we still have space to search 

        m = (l + r) // 2 # middle value

        if target == nums[m]:
            return m
        elif target > nums[m]: # target is in right half
            l = m + 1
            print(f'Looking for {target} in list {nums[l:r + 1]}')

        elif target < nums[m]: # target is in left half
            r = m - 1
            print(f'Looking for {target} in list {nums[l:m]}')

    return -1 


lst = [3, 5, 7, 8, 9, 10, 12, 14, 17, 19]

num = 17

result = binarySearch(lst, num)

if result != 1:
    print(f'Element {num} is present at index {result}')
else:
    print(f'Element {num} was not found in the list')