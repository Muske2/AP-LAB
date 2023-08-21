list1=input("Enter list 1: ")
list2=input("Enter list 2: ")
l1=list1.split()
l2=list2.split()
l3=[]
for i in l1:
    if int(i)%2!=0:
        l3.append(i)
for i in l2:
    if int(i)%2==0:
        l3.append(i)
print("LIST3: ",l3)
