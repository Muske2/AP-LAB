def fibo(n):
    a=0
    b=1
    i=1
    x=0
    while i<=n:
        if i==1:
            print("i=",i,0)
        elif i==2:
            print("i=",i,1)
        else:
            x=a+b
            a=b
            b=x
            print("i=",i,x)
        
        yield i
        i+=1


n=int(input('Enter n: '))
for i in fibo(n):
    print()
