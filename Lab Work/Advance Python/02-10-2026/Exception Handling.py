"""
try:
    n = int(input("Enter a number: "))
    if(n==0):
        print("Zero")
    else:
        print("Not Zero")
except ValueError as e:
    print("Error:", e)
else:
    print("Try Here!")
finally:
    print("Finally Here!, Thanks for using this program!!")
"""

try:
    n = int(input("Enter a number: "))
    if(n==0):
        print("Zero")
    else:
        print("Not Zero")
except Exception as e:
    print("Error:", e)
    print("Invalid input, please enter a valid integer.                                                     ")