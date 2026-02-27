def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiplication(x, y):
    return x * y

def division(x, y):
    return x / y

x = int(input("Enter first number: "))
operation = input("Select operation (+,-,*,/): ")
y = int(input("Enter second number: "))

if operation == "+":
    print(x, "+", y, "=", add(x, y))

elif operation == "-":
    print(x, "-", y, "=", subtract(x, y))

elif operation == "*":
    print(x, "*", y, "=", multiplication(x, y))

elif operation == "/":
    print(x, "/", y, "=", division(x, y))

else:
    print("Invalid input - Please restart")