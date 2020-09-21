#Sparse Matrices Transpose
#121910313046 - naveen chowdary
n= int(input('Enter the value of N in NxN Matrix : '))
a = []
#taking values of matrix:
for i in range(n):
    x = []
    print(f'Enter the values in {i}th row : ')
    for j in range(n):
        x.append(int(input()))

    a.append(x)
#Transposing the Matrix :
b = [[a[j][i] for j in range(n)]for i in range(n)]
print("The Transposed matrix : ")
for v in b:
    for e in v:
        print(e ,end ='  ')
    print()
#Printing the sparce matrix representation after transposing
sp2= []
for i in range(len(b)):
    for j in range(len(b[0])):
        if b[i][j] != 0 :
            temp = []
            temp.append(i)
            temp.append(j)
            temp.append(b[i][j])
            sp2.append(temp)

print('The Sparse Matrix Representation after Transposing :')
for i in sp2:
    for x in i:
        print(x , end=' \t ')
    print()
