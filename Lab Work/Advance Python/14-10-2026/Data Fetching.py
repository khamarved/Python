
from Database_Creation import *
import pymysql

mydb = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    database="python"
)

mycursor = mydb.cursor()

while True:
    menu = """
    Press 1 for Insert Data
    Press 2 for Update Data
    Press 3 for Delete Data
    Press 4 for Fetch Data
    Press 5 for Exit
    """

    print(menu)

    choice = int(input("Enter Choice: "))

    if choice == 1:
        name = input("Enter Name: ")
        mobile = input("Enter Mobile: ")

        query = "INSERT INTO python (name, mobile) VALUES (%s, %s)"
        args = (name, mobile)

        mycursor.execute(query, args)
        mydb.commit()

        print("Data Inserted Successfully!!")


    elif choice == 2:
        id = int(input("Enter ID: "))
        name = input("Enter Name: ")
        mobile = input("Enter Mobile: ")

        query = "UPDATE python SET name = %s, mobile = %s WHERE id = %s"
        args = (name, mobile, id)

        mycursor.execute(query, args)
        mydb.commit()

        if mycursor.rowcount > 0:
            print("Data Updated Successfully!!")
        else:
            print("ID Not Found!!")


    elif choice == 3:
        id = int(input("Enter ID: "))

        query = "DELETE FROM python WHERE id = %s"
        mycursor.execute(query, (id,))
        mydb.commit()

        if mycursor.rowcount > 0:
            print("Data Deleted Successfully!!")
        else:
            print("ID Not Found!!")


    elif choice == 4:
        query = "SELECT * FROM python"

        mycursor.execute(query)
        data = mycursor.fetchall()

        if data:
            for row in data:
                print(row)
        else:
            print("No Data Found!!")


    elif choice == 5:
        print("Thank You!!")
        break

    else:
        print("Invalid Choice! Please Enter 1 to 5.")

mycursor.close()
mydb.close()
