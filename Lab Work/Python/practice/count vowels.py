
text = input("Enter Text : ")

count = 0

for i in text:
    if i in "aeiou":
        count = count + 1

print("Number of vowels:", count)