dict={}
sen=input("Enter sentence: ")
words=sen.split()
k=1
for i in words:
    dict[k]=i
    k+=1
print("Number of words: "+str(k))
print(dict)
