# Factorial Number.

N = int(input("Enter Number : "))

factorial = 1

for i in range(1,N+1):
    factorial = factorial * i
    
print("The factorial Of The Number is : ",factorial)
    
    