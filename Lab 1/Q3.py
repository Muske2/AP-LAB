n=int(input('Enter value of n: '))
str=[]
for i in range(0,n):
    a=input("Enter string : ")
    str.append(a)
cnt=0
for i in str:
    if i[0]==i[len(i)-1] and len(i)>1:
        cnt+=1
    if len(i)%2!=0:
        print(i)
print("Strings with same first and last characters and having string length of 2 or more = ",cnt)
