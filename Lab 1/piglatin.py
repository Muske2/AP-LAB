def piglatin(text):
    words=text.split()
    ans=[]
    for word in words:
        ans.append(word[1:len(word)]+word[0]+"ay ")
    return ans
text=input('Enter: ')
result=piglatin(text)
print(' '.join(result))
