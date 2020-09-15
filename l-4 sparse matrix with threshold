a= int(input("Enter Number of rows"))
b= int(input("Enter columns"))
matrix=[]
for i in range (a):
    c=[]
    for j in range(b):
        j=int(input("Enter Number in matrix"+str(i)+" "+str(j)+" "))
        c.append(j)
    print()
    matrix.append(c)
for i in range (a):
    for j in range (b):
        print (matrix [i][j],end="")
        print()

thres=1
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j] <thres+1:
            matrix[i][j]=0
sparseMatrix = []
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j] != 0:
            temp = [i, j, matrix[i][j]]
            sparseMatrix.append(temp)
print(sparseMatrix)
