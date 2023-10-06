import re

f=open("q1.txt","w+")
f.write("Hello how are you today ?")
f.write("This is a sample text . how is the weather today ? how old are you ? How ? ok bye")
f.seek(0)
text=f.read()
text=text.lower()
words=text.split()
d={}
for word in words:
    if word=='.' or word==',' or word=='?':
        continue
    if word in d:
        d[word]=d[word]+1
    else:
        d[word]=1
print("number of occurences of words: ")
print(d)
