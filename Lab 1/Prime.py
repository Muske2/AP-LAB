n=int(input("Enter n: "))
m=int(input("Enter m: "))
for i in range(n,m+1):
    cnt=0
    for j in range(2,i//2 +1):
        if i%j==0 and i!=1:
            cnt+=1
    if cnt==0:
            print(i)
