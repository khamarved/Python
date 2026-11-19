"""Create a basic calculator program that takes two numbers and an operator (+, -, *, /) as input,
 performs the correct operation using typecasting, and prints the result. If the user enters
   an invalid operator, print an error message."""

a=float(input("Enter the first number: "))
b=float(input("Enter the second number: "))
operator=input("Enter an operator (+, -, *, /): ")
if operator=='+':
    print(f"Result: {a + b}")
elif operator=='-':
    print(f"Result: {a - b}")
elif operator=='*':
    print(f"Result: {a * b}")   
elif operator=='/':
    print(f"Result: {a / b}")
else:
    print("Error: Invalid operator")
