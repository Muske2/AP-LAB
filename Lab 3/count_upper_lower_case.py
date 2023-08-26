def countalpha(sen):
    up=0
    lo=0
    for i in sen:
        if i.isupper():
            up+=1
        elif i.islower():
            lo+=1
    print('No. of Upper case characters: '+str(up))
    print('No. of Lower case characters: '+str(lo))
    return

sen=input('Enter a string: ')
countalpha(sen)
