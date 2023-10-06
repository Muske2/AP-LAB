import re
f=open("input.txt","w+")
email=[]
email.append("happy@gmail.com")
email.append("rozie.com")
email.append("pinki@mit.edu")
email.append("rosa@")
email.append("hello23@worker.net")
for i in email:
    f.write(i+"\n")
validemail=[]
invalidemail=[]
pattern=r"[A-Za-z0-9].*@[A-Za-z].*\.(com|net|edu)"
for e in email:
    s=re.search(pattern,e)
    if s:
        validemail.append(e)
    else:
        invalidemail.append(e)

a=open("valid.txt","w+")
for i in validemail:
    a.write(i+"\n")
a.seek(0)
print(a.read())
a.close()
b=open("invalid.txt","w+")
for i in invalidemail:
    b.write(i+"\n")
b.seek(0)
print(b.read())
b.close()
f.close()
