
from tkinter import *
from tkinter import messagebox
import sqlite3
from login_Page import login

root = Tk()
root.geometry("500x500")
root.title("Registration Form!!")

# Database connection
def create_table():
    conn = sqlite3.connect("registration.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            mobile TEXT NOT NULL,
            password TEXT NOT NULL
        )
    """)

    # Add name column if an older version of the table exists
    cursor.execute("PRAGMA table_info(users)")
    columns = [row[1] for row in cursor.fetchall()]
    if "name" not in columns:
        cursor.execute("ALTER TABLE users ADD COLUMN name TEXT")

    conn.commit()
    conn.close()


create_table()


# Labels
Label(root, text="Enter Name : ", font=("Calibri", 14, "bold")).place(x=50, y=50)
Label(root, text="Enter Email : ", font=("Calibri", 14, "bold")).place(x=50, y=100)
Label(root, text="Enter Mobile : ", font=("Calibri", 14, "bold")).place(x=50, y=150)
Label(root, text="Enter Password : ", font=("Calibri", 14, "bold")).place(x=50, y=200)
Label(root, text="Enter Cpassword : ", font=("Calibri", 14, "bold")).place(x=50, y=250)


# Entry boxes
ename = Entry(root, bg="yellow")
ename.place(x=280, y=55)

eemail = Entry(root, bg="yellow")
eemail.place(x=280, y=105)

emobile = Entry(root, bg="yellow")
emobile.place(x=280, y=155)

epassword = Entry(root, bg="yellow", show="*")
epassword.place(x=280, y=205)

ecpassword = Entry(root, bg="yellow", show="*")
ecpassword.place(x=280, y=255)


# Insert data
def insert_data():
    name = ename.get().strip()
    email = eemail.get().strip()
    mobile = emobile.get().strip()
    password = epassword.get()
    cpassword = ecpassword.get()

    if not all([name, email, mobile, password, cpassword]):
        messagebox.showerror("Error", "Please fill all fields.")
        return

    if password != cpassword:
        messagebox.showerror("Error", "Passwords do not match.")
        return

    if not mobile.isdigit() or len(mobile) != 10:
        messagebox.showerror("Error", "Enter a valid 10-digit mobile number.")
        return

    conn = sqlite3.connect("registration.db")
    cursor = conn.cursor()

    try:
        cursor.execute("""
            INSERT INTO users (name, email, mobile, password)
            VALUES (?, ?, ?, ?)
        """, (name, email, mobile, password))

        conn.commit()
        messagebox.showinfo("Success", "Registration successful!")

    except sqlite3.IntegrityError:
        messagebox.showerror("Error", "This email is already registered.")

    finally:
        conn.close()


# Search data using email
def search_data():
    email = eemail.get().strip()

    if not email:
        messagebox.showerror("Error", "Enter an email to search.")
        return

    conn = sqlite3.connect("registration.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT name, email, mobile, password
        FROM users WHERE email = ?
    """, (email,))

    record = cursor.fetchone()
    conn.close()

    if record:
        ename.delete(0, END)
        ename.insert(0, record[0] or "")

        eemail.delete(0, END)
        eemail.insert(0, record[1])

        emobile.delete(0, END)
        emobile.insert(0, record[2])

        epassword.delete(0, END)
        epassword.insert(0, record[3])

        ecpassword.delete(0, END)
        ecpassword.insert(0, record[3])

        messagebox.showinfo("Success", "Record found!")
    else:
        messagebox.showerror("Error", "Record not found.")


# Update existing record using email
def update_data():
    name = ename.get().strip()
    email = eemail.get().strip()
    mobile = emobile.get().strip()
    password = epassword.get()
    cpassword = ecpassword.get()

    if not all([name, email, mobile, password, cpassword]):
        messagebox.showerror("Error", "Fill all fields. Search first if needed.")
        return

    if password != cpassword:
        messagebox.showerror("Error", "Passwords do not match.")
        return

    if not mobile.isdigit() or len(mobile) != 10:
        messagebox.showerror("Error", "Enter a valid 10-digit mobile number.")
        return

    conn = sqlite3.connect("registration.db")
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE users
        SET name = ?, mobile = ?, password = ?
        WHERE email = ?
    """, (name, mobile, password, email))

    conn.commit()
    updated = cursor.rowcount
    conn.close()

    if updated:
        messagebox.showinfo("Success", "Record updated!")
    else:
        messagebox.showerror("Error", "Email not found. Search first.")


# Delete record using email
def delete_data():
    email = eemail.get().strip()

    if not email:
        messagebox.showerror("Error", "Enter an email to delete.")
        return

    if not messagebox.askyesno("Confirm", "Delete this user?"):
        return

    conn = sqlite3.connect("registration.db")
    cursor = conn.cursor()

    cursor.execute("DELETE FROM users WHERE email = ?", (email,))

    conn.commit()
    deleted = cursor.rowcount
    conn.close()

    if deleted:
        messagebox.showinfo("Success", "Record deleted!")
        clear_fields()
    else:
        messagebox.showerror("Error", "Email not found.")


def clear_fields():
    for entry in (ename, eemail, emobile, epassword, ecpassword):
        entry.delete(0, END)


# Buttons
Button(
    root, fg="red", font=("Calibri", 18, "italic"),
    text="Insert", command=insert_data
).place(x=50, y=300)

Button(
    root, fg="red", font=("Calibri", 18, "italic"),
    text="Update", command=update_data
).place(x=140, y=300)

Button(
    root, fg="red", font=("Calibri", 18, "italic"),
    text="Delete", command=delete_data
).place(x=250, y=300)

Button(
    root, fg="red", font=("Calibri", 18, "italic"),
    text="Search", command=search_data
).place(x=350, y=300)

Button(
    root, text="Open Login Page",
    command=login
).place(x=170, y=380)

root.mainloop()
