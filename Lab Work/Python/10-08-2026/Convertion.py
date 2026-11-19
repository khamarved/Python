"""
    week  Month
    Days  Week
    year  Week
    Month Day    
    """
    
week= int(input("Enter Week: "))
print("Month are :", week/4)
days = int(input("Enter days: "))
print("Weeks are : ", days/7)
year = int(input("Enter Year: "))
print("Weeks are : ",year*52)
Month = int(input("Enter Month: "))
print("Days are : ",Month*30)