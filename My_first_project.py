'''calculator'''

def addition(a,b):
    return a+b

def substraction(a,b):
    return a-b

def multiplication(a,b):
    return a*b

def division(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        print(" divisor cannot be zero" )

try:
    a = float(input("enter the first number: "))
    b = float(input("enter the second number: "))
    c = str(input("enter the operation you want to perform:  +,-,*,/ \n"))

    if c == "+":
        print(f"{addition(a, b):.2f}")

    elif c == "-":
        print(f"{substraction(a,b):.2f}")

    elif c == "*":
        print(f"{multiplication(a,b):.2f}")

    elif c == "/":
        # if b == 0:
        #     print("enter value greater than zero ")
        # else:
            res = division(a,b)
            if res:
                print(f"{res:.2f}")
                   

    else: 
        print("enter the valid operation")
except ValueError:
    print("Enter a valid number")