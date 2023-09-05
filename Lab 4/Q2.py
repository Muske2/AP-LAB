import cmath

x=int(input("Enter real value of complex number: "))
y=int(input("Enter imaginary value of complex number: "))
z=complex(x,y)

print("Complex number= "+str(z.real)+" + "+str(z.imag)+"j")
print("Square root= "+str(cmath.sqrt(z)))
print("Log value= "+str(cmath.log(z)))
print("Sine value= "+str(cmath.sin(z)))
