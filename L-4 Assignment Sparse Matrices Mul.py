# Program to Multiply Sparse Matrices

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

# Function to multiply two sparse matrices
def mul(arr1,arr2):
    s1 = len(arr1)
    s2 = len(arr2)
    s3 = len(arr2[0])
    res = [[0 for _ in range(s3)] for __ in range(s1)]

    for i in range(s1):
        for j in range(s3):
            for k in range(s2):
                res[i][j] += arr1[i][k]*arr2[k][j]
    ans = sparse_matrix(res)
    return ans

# Function to print martix
def print_martix(arr):
    if arr==[]: print('EMPTY MATRIX')
    for i in arr:
        print(*i)

# Function to take array input
def input_matrix(r):
    arr = [] # Declaring the matrix
    i = 0
    while i<r:
        dup = list(map(int,input().split()))
        arr.append(dup)
        i += 1
    return arr


# Inputting arrays
s1 = int(input("Enter the number of rows in first matrix : "))
s2 = int(input("Enter the number of columns in first matrix : "))
s3 = int(input("Enter the number of rows in second matrix : "))
s4 = int(input("Enter the number of columns in second matrix : "))
if s2!=s3:
    print('You cannot multiply these matrices')
    exit()
print("Enter Martix 1")
arr1 = input_matrix(s1)
print("Enter Martix 2")
arr2 = input_matrix(s3)

# Printing Original Matrices
print("The Original Matrices are")
print("Matrix 1")
print_martix(arr1)
print("Matrix 2")
print_martix(arr2)
print()

# Printing Sparse Matrices
print("The Sparse Matrices are")
sp1 = sparse_matrix(arr1)
sp2 = sparse_matrix(arr2)
print("Sparse Matrix 1")
print_martix(sp1)
print("Sparse Matrix 2")
print_martix(sp2)
print()

# Printing the result
print("Multiplication of 2 Sparse Matrices")
result = mul(arr1,arr2)
print_martix(result)
