row=int(input("Enter number of rows: "))
col=int(input("Enter number of columns: "))
mat1={}
for i in range(row):
   for j in range(col):
       num=int(input("Enter value of row " +str(i+1)+" and column "+str(j+1)+ " for matrix 1: "))
       while num==0:
           print("Please enter non-zero value: ")
           num=int(input("Enter value of row " +str(i+1)+" and column "+str(j+1)))
       mat1[(i,j)]=num
print("MATRIX 1")
for i in range(row):
    for j in range(col):
        print(str(mat1[(i,j)]),end=" ")
    print("\n")
mat2={}
for i in range(row):
    for j in range(col):
        num=int(input("Enter value of row "+str(i+1)+" and column "+str(j+1)+" for matrix 2: "))
        while num==0:
            print("Please enter a non-zero value")
            num=int(input("Enter value of row "+str(i+1)+" and column "+str(j+1)+" for matrix 2: "))
        mat2[(i,j)]=num
print("MATRIX 2")
for i in range(row):
    for j in range(col):
        print(str(mat2[(i,j)]),end=" ")
    print("\n")
mat3={}
for i in range(row):
    for j in range(col):
        mat3[(i,j)]=mat1[(i,j)]+mat2[(i,j)]
print("SUM OF THE TWO MATRICES")
for i in range(row):
    for j in range(col):
        print(str(mat3[(i,j)]),end=" ")
    print("\n")
