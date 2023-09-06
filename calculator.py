#Addition
def add(x, y):
    return x + y
#Subtraction
def subtract(x, y):
    return x - y
#Multiplication
def multiply(x, y):
    return x * y
#Divition
def divide(x, y):
    if y == 0:
        raise ValueError("Error")
    return x / y
