def uniq(list1):
    unique=[]
    for num in list1:
        if num not in unique:
            unique.append(num)
    return unique


l=[]
n=int(input('Enter number of elements in list: '))
while n>0:
    l.append(input('Enter number: '))
    n-=1
print(l)
unique=uniq(l)
print('Unique List: ')
print(unique)
