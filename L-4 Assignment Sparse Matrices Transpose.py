# Program to Transpose a Sparse Matrix
# 121910313046 - naveen chowdary

# Function to represent the Sparse Matrix
def sparse_matrix(arr):
    sp = []
    a = len(arr)
    b = len(arr[0])
    # Finding the non zero elements
    for i in range(a):
        for j in range(b):
            if arr[i][j]!=0:
                sp.append([i,j,arr[i][j]])
    return sp

# Function to transpose sparse matrix
def trans(arr):
    res = []
    for i in arr:
        res.append([i[1],i[0],i[2]])
    res.sort()
    return res


# Function to print martix
def print_martix(arr):
    if arr==[]: print("Empty Matrix")
    for i in arr:
        print(*i)

arr = [] # Declaring the matrix

# Taking the matrix input
a = int(input("Enter the number of rows : "))
b = int(input("Enter the number of columns : "))
for i in range(a):
    dup = list(map(int,input().split()))
    arr.append(dup)

print("The Original Matrix")
print_martix(arr)

print()

# Printing the sparse matrix
sparse = sparse_matrix(arr)
print("The Sparse Matrix")
print_martix(sparse)

# Printing the transpose of a sparse matrix
transpose = trans(sparse)
print("The Transpose of the Sparse Matrix")
print_martix(transpose)
