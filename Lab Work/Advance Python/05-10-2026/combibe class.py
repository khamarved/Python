class NumberCheck:
    
    def even(self, num):
        if num % 2 == 0:
            return "Even Number"
        else:
            return "Not an Even Number"

    def odd(self, num):
        if num % 2 != 0:
            return "Odd Number"
        else:
            return "Not an Odd Number"

    def palindrome(self, num):
        original = num
        reverse = 0

        while num > 0:
            digit = num % 10
            reverse = reverse * 10 + digit
            num = num // 10

        if original == reverse:
            return "Palindrome Number"
        else:
            return "Not a Palindrome Number"


obj = NumberCheck()

num = int(input("Enter a number: "))

print(obj.even(num))
print(obj.odd(num))
print(obj.palindrome(num))