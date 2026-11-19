
n = int(input("Enter Number : "))
prime = True
if n < 2:
    prime = false
else :
    for i in range(2,n):
        if n%i == 0:
            prime = false
            break
        
if prime:
    print("the Number Is prime!!")
else:
    print("The Number Is Not Prime!!")