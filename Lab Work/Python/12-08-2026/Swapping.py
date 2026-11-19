
#Swapping Are Of Two Types.

#With using third variable.
#Without using third variablr.

a = int(input("Enter Number 1 : "))
b = int(input("Enter Number 2 : "))


#METHOD 1.
# a= 100 , b= 50
"""
temp = a      
a = b
b = temp

print("Value Of A :",a)
print("Value Of B :",b)"""

#METHOD 2.

# a=a+b    100+50  a=150
# b=a-b    150-50  b=100
# a=a-b    150-100 a=50


#METHOD 3.

a, b = b,a
print("Value Of A :",a)
print("Value Of B :",b)

