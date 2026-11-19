import random
otp = random.randint(1000, 9999)
d={}
while True:
    menu = """
     1.sign up
     2.sign in
     3.exit
    """
    print(menu)
    try:
        n = int(input("Enter Your choice :"))
    except Exception as e :
        print("Something went wrong!")
        continue
    if n==1:
            name = input("Enter Your Name :")
            email = input("Enter Your Email :")
            mobile = input("Enter Your Mobile Number :")
            password = input("Enter Your Password :")
            cpasssword = input("Enter Your Confirm Password :")
            if password==cpassword:
                d['email'] = email
                d['mobile'] = mobile
                d['password'] = password
                print("Sign Up Successfully!")
            else:
                print("Passwords do not match!")
    elif n==2:
        try:
             email = input("Enter Your Email :")
             password = input("Enter Your Password :")
             if email==d['email'] and password==d['password']:
                print("Sign In Successfully!")
             else:
              print("Invalid Email or Password!")
        except Exception as e:
          print("Something went wrong!")
    elif n==3:
        try:
            mobile = input("Enter Your Mobile Number :")
            if d['mobile']==mobile:
                print("Your OTP is :",otp)
                user_otp = int(input("Enter Your OTP :"))
                if user_otp==otp:
                    password = input("Enter Your New Password :")
                    cpassword = input("Enter Your Confirm Password :")
                    if password==cpassword:
                        d['password'] = password
                        print("Password Updated Successfully!")
                    else:
                        print("Passwords do not match!")
                else:
                    print("Invalid OTP!")
            else:
                print("Invalid Mobile Number!")
        except Exception as e:
            print("Something went wrong!",e)
    elif n==4:
        print("Exiting...")
        break
    else:
        print("Invalid Choice! please enter 1 to 4.")