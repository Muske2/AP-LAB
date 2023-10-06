f=open("game.txt","r")
text=f.readlines()
for i in text:
    print(i[::-1])

line=text[::-1]
print(line)
