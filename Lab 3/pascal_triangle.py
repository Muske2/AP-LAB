def pascal(n):
    triangle=[]
    for i in range(n):
        row=[1]*(i+1) #initialize all elements of the row to 1
        if i>=2:
            for j in range(1,i):
                row[j]=triangle[i-1][j]+triangle[i-1][j-1]
        triangle.append(row)
    return triangle

def print_pascal(tr):
    for row in tr:
        print(" ".join(map(str,row)).center(len(tr[-1])*3))
    return

n=int(input('Enter number of rows: '))
tr=pascal(n)
print_pascal(tr)
        
              
        
        
