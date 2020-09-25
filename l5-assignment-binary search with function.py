#binary search with function and dynamic input
#definition for binary search function
def binary_search(a, x): 
	low = 0
	high = len(a) - 1
	mid = 0
	while low <= high: 
		mid = (high + low) // 2
		if a[mid] < x: 
			low = mid + 1
		elif a[mid] > x: 
			high = mid - 1
		else: 
			return mid  
	return -1
a=[]
n=int(input("enter number of elements to be entered into array: "))
for i in range(0,n):
    x=int(input("enter the element:"))
    a.append(x)  
x=int(input("enter the value to be searched:"))
result = binary_search(a, x)
#printing index of the searched element
if(result != -1):
    print("Element is present at index", str(result))  
else:
    print("element not found")
