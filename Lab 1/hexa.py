hexa=input("Enter number: ")
ls=['a','A','b','B','c','C','d','D','e','E','f','F','0','1','2','3','4','5','6','7','8','9']
flag=0
for i in hexa:
   if i not in ls:
      flag=1
if flag==1:
    print("no")
else:
    print("yes")
    
