from tkinter import *

root=Tk()
root.title("Calculator")

e=Entry(root,width=35)
e.grid(row=0,column=0,columnspan=3,padx=10,pady=20)
def button_click(num):
    n=e.get()
    e.delete(0,END)
    e.insert(0,str(n)+str(num))

def button_clear():
    e.delete(0,END)

def button_add():
    a=e.get()
    global fnum
    global math
    math="add"
    fnum=int(a)
    e.delete(0,END)

def button_equal():
    b=e.get()
    e.delete(0,END)
    if math=="add":
         e.insert(0,fnum+int(b))
    if math=="subtract":
         e.insert(0,fnum-int(b))
    if math=="multiply":
         e.insert(0,fnum*int(b))
    if math=="divide":
         e.insert(0,fnum/int(b))

def button_sub():
     a=e.get()
     global fnum
     global math
     math="subtract"
     fnum=int(a)
     e.delete(0,END)

def button_mult():
     a=e.get()
     global fnum
     global math
     math="multiply"
     fnum=int(a)
     e.delete(0,END)

def button_divide():
     a=e.get()
     global fnum
     global math
     math="divide"
     fnum=int(a)
     e.delete(0,END)
    
b1=Button(root,text="1",padx=40,pady=20,command=lambda:button_click(1))
b2=Button(root,text="2",padx=40,pady=20,command=lambda:button_click(2))
b3=Button(root,text="3",padx=40,pady=20,command=lambda:button_click(3))
b4=Button(root,text="4",padx=40,pady=20,command=lambda:button_click(4))
b5=Button(root,text="5",padx=40,pady=20,command=lambda:button_click(5))
b6=Button(root,text="6",padx=40,pady=20,command=lambda:button_click(6))
b7=Button(root,text="7",padx=40,pady=20,command=lambda:button_click(7))
b8=Button(root,text="8",padx=40,pady=20,command=lambda:button_click(8))
b9=Button(root,text="9",padx=40,pady=20,command=lambda:button_click(9))
b0=Button(root,text="0",padx=40,pady=20,command=lambda:button_click(0))
badd=Button(root,text="+",padx=40,pady=20,command=button_add)
bsub=Button(root,text="-",padx=40,pady=20,command=button_sub)
bmult=Button(root,text="x",padx=40,pady=20,command=button_mult)
bdivide=Button(root,text="/",padx=40,pady=20,command=button_divide)
bequal=Button(root,text="=",padx=40,pady=20,command=button_equal,bg="green")
bclear=Button(root,text="Clear",padx=79,pady=20,command=button_clear)

#Put buttons on the screen
b1.grid(row=3,column=0)
b2.grid(row=3,column=1)
b3.grid(row=3,column=2)
b4.grid(row=2,column=0)
b5.grid(row=2,column=1)
b6.grid(row=2,column=2)
b7.grid(row=1,column=0)
b8.grid(row=1,column=1)
b9.grid(row=1,column=2)
b0.grid(row=4,column=0)
badd.grid(row=5,column=0)
bsub.grid(row=5,column=1)
bmult.grid(row=6,column=0)
bdivide.grid(row=6,column=1)
bequal.grid(row=5,column=2)
bclear.grid(row=4,column=1,columnspan=2)
