# Factor program using the for loop

n = int(input("Enter Number : "))
fac = 1
for i in range(1,n+1):
    fac = fac * i
print("Factorial = ",fac)