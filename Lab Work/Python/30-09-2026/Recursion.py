# Recursion
"""
-> When the function call itself it is called Recursion.
-> It is used id DSA ,  Coding
->Eg = Keyboard


-> D.S.A : Types Of D.S.A
1. Base Condition
2. Recursive : Programs
. Recursion
"""
def fac(n):
    if n == 1:
        return 1
    else:
        return n * fac(n - 1)

print(fac(5))