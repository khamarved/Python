#Function with Paliondrome Number;
def Palindrome_Number():
     n = int(input("Enter Number :"))
     rem = 0
     rev = 0
     n1=n
     while(n!=0):
       rem = n%10
       rev = rev*10+rem
       n//=10
#print(rev)
     if(n1 == rev):
      print("Palindrome!!")
     else :
      print("Not Palindrome!!")
 
Palindrome_Number()