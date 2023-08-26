def multlist(list1):
    product=1
    for num in list1:
        product*=int(num)
    return product
l=[]
n=int(input('Enter number of elements in list: '))
while n>0:
    l.append(input('Enter number: '))
    n-=1
print(l)
prod=multlist(l)
print('Product= '+str(prod))
