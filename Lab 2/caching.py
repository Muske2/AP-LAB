#demonstrate caching with dictionaries
def fib(n):
    if n in fib.cache:
        return fib.cache[n]
    else:
        fib.cache[n]=fib(n-1)+fib(n-2)
        return fib.cache[n]
fib.cache={0:0,1:1}
print("FIBONACCI FUNCTION")
n=int(input("Enter n: "))
print(fib(n))
      
      
