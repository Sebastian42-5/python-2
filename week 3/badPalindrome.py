def isPalindrome(lst):
    '''
    determine if lst is a palindrome 
    param lst: lst is a list
    return: True if lst is a palindrome, False otherwise
    '''
    temp = lst[:]
    temp.reverse()
    print(temp, lst)
    return temp == lst

def silly(n):
    '''
    get n inputs from user. Print 'yes' if the sequence of inputs forms a palindrom, 'no' otherwise
    param n: n is an integer > 0
    return: None
    '''
    result = []
    for i in range(n):
        elem = input('Enter element: ')
        result.append(elem)

    if isPalindrome(result):
        print('Yes')
    else:
        print('No')

silly(2)