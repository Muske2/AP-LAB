listo=input("Enter List 1 elements: ")
lists=input("Enter List 2 elements: ")
list1=listo.split()
list2=lists.split()
list3=[]
#print('List 1: ',list1)
for i in range(len(list1)):
    list1[i]=int(list1[i])
for i in range(len(list2)):
    list2[i]=int(list2[i])
for i in list1:
    if i%2!=0:
        list3.append(i)
for i in list2:
    if i%2==0:
       list3.append(i)
print(list3)

