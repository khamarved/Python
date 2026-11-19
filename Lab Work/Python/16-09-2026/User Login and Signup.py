#User login and signup page 

import random

otp = random.randint(1001, 9999)

while True:
    menu  = """
    press 1 for login
    press 2 for signup
    press 3 for update password
    press 4 for Exit
    """
    print(menu)
    choice = int(input("Enter choice : "))
    if choice == 1:
            