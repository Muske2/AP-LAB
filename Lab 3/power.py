def power(x,r):
    p=1
    while r>0:
        p*=x
        r-=1
    return p
print("COMPUTE x TO THE POWER OF r")
x=int(input("Enter x: "))
r=int(input("Enter r: "))
print(power(x,r))
