import string

sen=input("Enter string: ")
words=sen.split()
ans=[]
for word in words:
    m=word.capitalize()
    ans.append(m)
print("Result: ")
for i in ans:
    print(i,end=" ")

