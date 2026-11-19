#Fibo Series Debugging

def fibo(n):
    if n==0:
        return 0
    if n==1:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)
for i in range(11):     
 print(fibo(i))
 
"""Debugging
 
 fibo(0) = 0
 fibo(1) = 1
 fibo(2) = 1
 fibo(3) = 2
 fibo(4) = 3
 fibo(5) = 5
 fibo(6) = 8
 fibo(7) = 13
 fibo(8) = 21
 fibo(9) = 34
 fibo(10) = 55
"""