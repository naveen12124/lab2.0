#program for binary search
arr = [1,20,22,35,67]
#taking input from user
x = int(input("Enter the element to search: "))
l = 0
h = len(arr)-1
flag = 0
mid = (h+l)//2

if x == arr[mid]:
    flag = 1
    loc = mid
    
elif x < arr[mid]:
    l = 0
    h = mid
    for i in range(l,h):
        if x == arr[i]:
            loc = i
            flag = 1
            break
else:
    l = mid+1
    h = len(arr)
    for i in range(l,h):            
        if x == arr[i]:
            loc = i
            flag = 1
            break
if flag == 1:
    print("Element found at " + str(loc))
else:    
    print("Element not found"
