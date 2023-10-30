#!/usr/bin/env python
# coding: utf-8

# In[1]:


def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ZeroDivisionError("Division by zero is not allowed.")
    return x / y

def calculate():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        print("Choose operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Modulus (%)")

        choice = input("Enter operation (1/2/3/4/5): ")

        if choice not in ['1', '2', '3', '4', '5']:
            raise ValueError("Invalid operation choice.")

        if choice == '1':
            result = add(num1, num2)
            operation = "+"
        elif choice == '2':
            if num1 < num2:
                raise ValueError("Subtraction with the first number lesser than the second is not allowed.")
            result = subtract(num1, num2)
            operation = "-"
        elif choice == '3':
            result = multiply(num1, num2)
            operation = "*"
        elif choice == '4':
            result = divide(num1, num2)
            operation = "/"
        elif choice == '5':
            result = num1 % num2
            operation = "%"

        print(f"Result: {num1} {operation} {num2} = {result}")

    except ValueError as ve:
        print(f"Error: {ve}")
    except ZeroDivisionError as zde:
        print(f"Error: {zde}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    calculate()


# In[ ]:




