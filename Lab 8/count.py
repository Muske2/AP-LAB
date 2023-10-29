from tkinter import *

root=Tk()
root.title("Counter")
x=0
def increment():
    global x
    x=x+1
    myLabel.config(text="Count= "+str(x))

def click():
    l2.config(text="BYE")
    
b1=Button(root,text="Click me!",command=increment,bg="pink")
b1.pack()
myLabel=Label(root,text="Count= "+str(x))
myLabel.pack()

b2=Button(root,text="EXIT",command=click)
b2.pack()
l2=Label(root,text="HELLO")
l2.pack()

root.mainloop()




