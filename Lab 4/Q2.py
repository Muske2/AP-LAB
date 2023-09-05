import cmath

x=int(input("Enter real value of complex number: "))
y=int(input("Enter imaginary value of complex number: "))
z=complex(i,j)

print("Complex number= "+str(z.real)+" + "+str(z.imag)+"j")
print("Square root= "+str(cmath.sqrt(z)))
print("Log value= "+str(cmath.log2(z)))
print("Sine value= "+str(cmath.sin(z)))
