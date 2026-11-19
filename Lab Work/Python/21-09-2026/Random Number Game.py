# Random Number Game 
import random

"""
    Lucky = random.randit(1,51)
    L = [45454,55641,144444,48584]
    Lucky = random.choice(L)
    print(Lucky)
    """
    
Lucky = random.randint(1,51)
while True:
    print("******Enter Number Between 1 to 50*******")
    choice = int(input("Enter Number : "))
    
    if choice > 50:
        print("Invalid Number!!!")
        break
    elif choice == Lucky:
        print("Congratulations!!!")
    elif Lucky > choice:
        print("The Lucky Number Is Bigger!!")
    else:
        print("The Lucky Number Is Smaller!!")                