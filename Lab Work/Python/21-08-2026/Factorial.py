#Factorial Number : 5*4*3*2*1 = 120

n = int(input("Enter Number : "))
fac = 1

i = 1
while(i<=n):
    fac=fac*i
    i=i+1
print(fac)