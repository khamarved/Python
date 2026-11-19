#Count Vowels in String
s = input("Enter String :")

count=0
for ch in s:
 if  ch in "aeiouAEIOU":
    print(ch)
    count = count+1
print("Total Vowels :", count)