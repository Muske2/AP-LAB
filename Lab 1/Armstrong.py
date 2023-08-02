num=input("Enter number: ")
length=len(num)
n=int(num)
arm=0
for i in num:
    arm+=int(i)**length
if n==arm:
    print("It is an Armstrong number.")
else:
    print("It is not an Armstrong number.")
