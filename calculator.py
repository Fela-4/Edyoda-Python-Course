# This program is about emulating a simple calculator
# that does Basic arithmetic operations.

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 == 0:
        return "Cannot divide by zero"
    
    else:
        return num1 / num2
    
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

sum_result = add(num1, num2)
sub_result = subtract(num1, num2)
mul_result = multiply(num1 , num2)
div_result = divide(num1 , num2)

print(f"Addition: {sum_result} \nSubtraction: {sub_result} \nMultiplication{mul_result} \nDivision:{div_result}")
