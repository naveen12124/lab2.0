#Defining the function binary Search
def binary_Search (a, s):
    high = len(a)
    low = 0
    mid = (low+high) //2
    a.sort()
    if s not in a:
        print ( 'Element not found in the array! !')
    elif a [mid] == s:
        print (' Element found at index',mid)
    elif s < a[mid]:
        for i in range (low, mid) :
            if a [i] == s:
                print (f'Element found at index (1)')
                break
    else:
        for i in range (mid, high):
            if a[i] == s:
                print (f' Element found at index (i)')
                break
#Test Case 1 : entering or passing the element that is not present in
print ( 'Test case 1: ')
arrl = [78, 99, 66, -99425, 33, 45]
s1 = -63
binary_Search (arrl, s1)

#Test Case 2 : Entering the middle element of the array
print ( 'Test case 2 : ')
arr2 = [-99, 88, 4963, 2357, -12, 0]
s2= 88
binary_Search (arr2, s2)

#Test Case 3 : Entering same number twice
print ( 'Test case 3 : ' )
arr3 = [0, 22, 555, 2253, 0, 565, -9486]
s3 = 0
binary_Search (arr3, s3)
