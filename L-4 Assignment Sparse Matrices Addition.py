# Sparse Matrices Addition
#121910313046 - naveen chowdary
p = int(input('Enter the value of N in NxN matrix: '))

print('''\nThis is a Sparse matrix input high frequency of zeros.\n''')
print("Enter the values for the first matrix : ")
u= []
for i in range(p):
    print('Enter the values for {i}th row : ')
    x=[]
    for j in range(p):
      x.append(int(input()))
    u.append(x)
#taking input
print('Enter the values for the Second Matrix :')
c =[]
for i in range(p):
    print(f'Enter the values for {i}th row : ')
    x=[]
    for j in range (p):
        x.append(int(input()))
    c.append(x)

#creating a matrix to store
p = [[0 for j in range(p)] for i in range(p)]
#adding two sparse matrices
for i in range(len(u)):
    for j in range(len(u[0])):
        p[i][j] = u[i][j] + c[i][j]

print('The sum of the two sparse matrices is :')
for r in p:
    for y in r:
        print(y, end = " ")
    print()
#representing the sparse matrix:
sparse_matrix = []
for i in range(len(p)):
    for j in range(len(p[0])):
        if p[i][j] != 0 :
            temp = []
            temp.append(i)
            temp.append(j)
            temp.append(p[i][j])
            sparse_matrix.append(temp)

print('''The Sparse Matrix representation :
Row\tCol\tValue''')
for i in sparse_matrix:
    for j in i:
        print(j,end = ' \t ')
    print()
