"""Create a small program that takes two numbers as input (use input()), 
converts them to integers using int(), and 
prints their sum, difference, product, and quotient using print().<br><br><em><strong>Hint:</strong>
 Remember to convert the input strings to integers before performing arithmetic operations.</em>"""

a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
print("Sum:", a + b)
print("Difference:", a - b)
print("Product:", a * b)
if b != 0:
    print("Quotient:", a / b)
