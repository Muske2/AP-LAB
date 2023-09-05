import datetime

name=input("What is your name? ")
now=datetime.datetime.now()
print("Current Time: "+now.strftime("%H:%M:%S"))
if now.hour<12:
    print("Good Morning "+name+"!")
elif 12<=now.hour<16:
    print("Good Afternoon "+name+"!")
else:
    print("Good Evening "+name+"!")
