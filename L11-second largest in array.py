def bubblesort(a):
	i = 0
	while i<2:
		for j in range(len(a)-1-i):
			if a[j]>a[j+1]:
				swap = True
				a[j],a[j+1] = a[j+1],a[j]
		i+=1
	print("second largest : ",a[-2])

print("Enter the array of elements : ")
arr = list(map(int,input().split()))
bubblesort(arr)
