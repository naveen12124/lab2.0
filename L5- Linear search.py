#program for linear search
arr = [2,18,24,35]
flag = 0
#taking input
x = int(input("Enter the element to search: "))
for i in range(len(arr)):
    if arr[i] == x :
       flag = 1
       break      
if flag == 1:        
    print('Element found at '+ str(i))    
else:
    print('Element not found'
