class Bank:
    def ac_register(self):
        name = input("Enter Name: ")
        self.password = input("Create Password: ")
        self.mobile = input("Enter Mobile Number: ")

        self.bal = 50000
        self.ac_no = 12345

        print("Account Opened Successfully!")
        print("Welcome,", name)
        print("Account Number:", self.ac_no)
        print("Initial Balance:", self.bal)

    def verify_account(self):
        account = int(input("Enter Account Number: "))
        password = input("Enter Password: ")

        if account == self.ac_no and password == self.password:
            return True
        else:
            print("Invalid Account Number or Password!")
            return False

    def deposit(self):
        if self.verify_account():
            damount = int(input("Enter Amount to Deposit: "))

            if damount <= 0:
                print("Enter a valid amount!")
            elif damount > 50000:
                print("You cannot deposit more than 50000 at a time!")
            else:
                self.bal += damount
                print("Deposit Successfully!")
                print("Current Balance:", self.bal)

    def withdraw(self):
        if self.verify_account():
            wamount = int(input("Enter Amount to Withdraw: "))

            if wamount <= 0:
                print("Enter a valid amount!")
            elif wamount > 20000:
                print("You cannot withdraw more than 20000 at a time!")
            elif wamount > self.bal:
                print("Insufficient Balance!")
            else:
                self.bal -= wamount
                print("Withdraw Successfully!")
                print("Current Balance:", self.bal)

    def check_balance(self):
        if self.verify_account():
            print("Current Balance:", self.bal)


obj = Bank()

menu = """
Press 1 for Account Opening
Press 2 for Exit
"""

print(menu)
choice = int(input("Enter Choice: "))

if choice == 1:
    obj.ac_register()

    while True:
        menu1 = """
Press 1 for Deposit
Press 2 for Withdraw
Press 3 for Check Balance
Press 4 for Exit
"""
        print(menu1)
        choice1 = int(input("Enter Choice: "))

        if choice1 == 1:
            obj.deposit()

        elif choice1 == 2:
            obj.withdraw()

        elif choice1 == 3:
            obj.check_balance()

        elif choice1 == 4:
            print("Thank You for Using Our Bank!")
            break

        else:
            print("Invalid Choice!")

elif choice == 2:
    print("Thank You!")

else:
    print("Invalid Choice!")
