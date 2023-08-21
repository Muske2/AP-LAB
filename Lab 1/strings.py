n=int(input("Enter number of strings: "))
i=0
sen=[]
cnt=0
while i<n:
    sen.append(input("Enter string "+str(i+1)+" : "))
    i+=1
print("Strings having odd length: ")
for i in sen:
    if i[0]==i[len(i)-1] and len(i)>1:
        cnt+=1
    if len(i)%2!=0:
        print(i)
print("Number of strings with same first and last characters and having the string length of 2 or more :" +str(cnt))
