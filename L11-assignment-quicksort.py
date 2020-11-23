def Quicksort(arr):
	if len(arr)<2: return arr
	point = 0
	# Partition
	for i in range(1,len(arr)):
		if arr[i]<arr[0]:
			point+=1
			arr[i],arr[point] = arr[point],arr[i]
	arr[0],arr[point] = arr[point],arr[0]

	#Recursion
	left = Quicksort(arr[:point])
	right = Quicksort(arr[point+1:])

	arr = left + [arr[point]] + right #Merging everything together
    
    return arr

# Taking Input
arr = list(map(int,input("Enter the array elements : ").split()))
Quicksort(arr)
