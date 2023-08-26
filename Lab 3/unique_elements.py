def uniq(list1):
    result=list(set(list1))
    return result

l=[]
n=int(input('Enter number of elements in list: '))
while n>0:
    l.append(input('Enter number: '))
    n-=1
print(l)
unique=uniq(l)
print('Unique List: ')
print(unique)
                
