#Sparse Matrices Multiplication
#121910313046 - naveen chowdary
d = int(input('Enter the value of d in matrix: '))

print('''\nThis is a Sparse matrix.
input high frequency of zeros.\n''')
#taking input
print(" please Enter the values of first matrix : ")
p= []
for i in range(d):
    print('Enter the values for {i}th row : ')
    x=[]
    for j in range(d):
      x.append(int(input()))
    p.append(x)
# taking values of 2nd matrix:
print('Enter the values for the Second Matrix :')
z =[]
for i in range(d):
    print(f'Enter the values for {i}th row : ')
    x=[]
    for j in range (d):
        x.append(int(input()))
    z.append(x)

#creating a matrix to store
d = [[0 for j in range(d)] for i in range(d)]
#adding two sparse matrices
for i in range(len(p)):
    for j in range (len(z[0])):
        for k in range (len(z)):
            d[i][j] += p[i][k] * z[k][j]


print('The sum of the two sparse matrices is :')
for r in d:
    for y in r:
        print(y, end = " ")
    print()
#representing the sparse matrix:
sparse_matrix = []
for i in range(len(d)):
    for j in range(len(d[0])):
        if d[i][j] != 0 :
            temp = []
            temp.append(i)
            temp.append(j)
            temp.append(d[i][j])
            sparse_matrix.append(temp)

print('The Sparse Matrix representation is:')
for i in sparse_matrix:
    for j in i:
        print(j,end = ' \t ')
    print()
