#linear search with functions and dynamic input
#121910313046
#implementing an array
a=[]
#taking input from user
n=int(input("enter number of elements to be entered into array: "))
for i in range(0,n):
    x=int(input("enter the element:"))
    a.append(x)
def linearsearch(a, x):
   for i in range(len(a)):
      if a[i] == x:
         return i
   return 'not found'
x=int(input("enter the value to be searched:"))
print("element found at index "+str(linearsearch(a,x)))
