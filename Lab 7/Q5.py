import re

str=input("Enter string: ")
pattern=r"^[a-zA-Z]$|^([a-zA-Z]).*\1$"
s=re.search(pattern,str,re.I)
if s:
    print("YES")
else:
    print("NO")
