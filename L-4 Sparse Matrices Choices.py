# Program to perform functions on Sparse Matrix
# 121910313046 - naveen chowdary

# Function to represent the Sparse Matrix
def sparse_matrix(arr):
    sp = []
    a = len(arr)
    b = len(arr[0])
    # Finding the non zero element
    for i in range(a):
        for j in range(b):
            if arr[i][j]!=0:
                sp.append([i,j,arr[i][j]])
    return sp

# Function to add two sparse matrices
def add(arr1,arr2):
    res = []
    l1 = len(arr1)
    l2 = len(arr2)
    if l1==0 : res = arr2
    if l2==0 : res = arr1
    i = 0
    j = 0
    while l1>0 and l2>0:
        if arr1[i][0]==arr2[j][0] and arr1[i][1]==arr2[j][1]:
            res.append([arr1[i][0],arr1[i][1],arr1[i][2]+arr2[j][2]])
            i += 1
            j += 1
        else:
            m = min(arr1[i],arr2[j])
            res.append(m)
            if m==arr1[i]:
                i += 1
            else:
                j += 1
        if i>=l1:
            for x in range(j,l2):
                res.append(arr2[x])
            break
        if j>=l2:
            for x in range(i,l1):
                res.append(arr1[x])
            break
    return res

# Function to multiply two sparse matrices
def mul(arr1,arr2):
    r1 = len(arr1)
    r2 = len(arr2)
    c2 = len(arr2[0])
    res = [[0 for _ in range(c2)] for __ in range(r1)]

    for i in range(r1):
        for j in range(c2):
            for k in range(r2):
                res[i][j] += arr1[i][k]*arr2[k][j]
    ans = sparse_matrix(res)
    return ans

# Function to transpose sparse matrix
def trans(arr):
    res = []
    for i in arr:
        res.append([i[1],i[0],i[2]])
    res.sort()
    return res

# Function to print martix
def print_martix(arr):
    if arr==[]: print("EMPTY MATRIX")
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
r = int(input("Enter the size of the square matrix : "))
print("Enter Martix 1")
arr1 = input_matrix(r)
print("Enter Martix 2")
arr2 = input_matrix(r)
print()

sp1 = sparse_matrix(arr1)
sp2 = sparse_matrix(arr2)

# Taking choice from user
print("Choose an operation from below")
print("1. Display the Sparse Matrices \n2. Addition of the Matrices \n3. Multiplication of the Matrices \n4. Transpose of the Matrices")
n = int(input("Enter an option : "))

if n==1:
    # Printing Sparse Matrices
    print("The Sparse Matrices are")
    print("Sparse Matrix 1")
    print_martix(sp1)
    print("Sparse Matrix 2")
    print_martix(sp2)
    print()
elif n==2:
    # Printing the Sum of Sparse Matrices
    print("Addition of 2 Sparse Matrices")
    result = add(sp1,sp2)
    print_martix(result)
elif n==3:
    # Printing the Product of Sparse Matrices
    print("Multiplication of 2 Sparse Matrices")
    result = mul(arr1,arr2)
    print_martix(result)
elif n==4:
    # Printing the Transpose of Sparse Matrices
    print("Transpose of the Matrices")
    print("Transpose of Sparse Matrix 1")
    print_martix(trans(sp1))
    print("Transpose of Sparse Matrix 2")
    print_martix(trans(sp2))
