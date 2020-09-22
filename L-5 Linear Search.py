#program for linear search
#121910313046
def linearsearch(arr, x):
   for i in range(len(arr)):
      if arr[i] == x:
         return i
   return -1
arr = ['p','y','t','h','o','n',]
x = 'o'
print("element found at index "+str(linearsearch(arr,x)))
