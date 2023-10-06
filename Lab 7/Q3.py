f=open("input.txt","w+")
f.write('''She sells seashells on the seashore;\n The shells that she sells are seashells I'm sure. \nSo if she sells seashells on the seashore, \nI'm sure that the shells are seashore shells''')
f.seek(0)
text=f.read()
lines=text.splitlines()
line=lines[::-1]
for i in line:
    print(i)
