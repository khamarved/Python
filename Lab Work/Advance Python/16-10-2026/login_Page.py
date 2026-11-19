
from tkinter import *
from tkinter import messagebox
import sqlite3


def login(parent=None):
    # Create login window
    if parent is None:
        window = Tk()
    else:
        window = Toplevel(parent)

    window.geometry("500x350")
    window.title("Login Page")

    Label(
        window, text="Login Page",
        font=("Calibri", 20, "bold")
    ).place(x=170, y=30)

    Label(
        window, text="Enter Email",
        font=("Calibri", 14, "bold")
    ).place(x=50, y=100)

    Label(
        window, text="Enter Password",
        font=("Calibri", 14, "bold")
    ).place(x=50, y=150)

    Label(
        window, text="Confirm Password",
        font=("Calibri", 14, "bold")
    ).place(x=50, y=200)

    email_entry = Entry(window, bg="lightblue")
    email_entry.place(x=280, y=105)

    password_entry = Entry(window, bg="lightblue", show="*")
    password_entry.place(x=280, y=155)

    cpassword_entry = Entry(window, bg="lightblue", show="*")
    cpassword_entry.place(x=280, y=205)

    def confirm_login():
        email = email_entry.get().strip()
        password = password_entry.get()
        cpassword = cpassword_entry.get()

        if not email or not password or not cpassword:
            messagebox.showerror(
                "Error", "Please fill all fields.",
                parent=window
            )
            return

        if password != cpassword:
            messagebox.showerror(
                "Error", "Passwords do not match.",
                parent=window
            )
            return

        conn = sqlite3.connect("registration.db")
        cursor = conn.cursor()

        cursor.execute(
            "SELECT id FROM users WHERE email=? AND password=?",
            (email, password)
        )

        result = cursor.fetchone()
        conn.close()

        if result:
            messagebox.showinfo(
                "Success", "Login Successful!",
                parent=window
            )
        else:
            messagebox.showerror(
                "Error", "Invalid email or password. Register first.",
                parent=window
            )

    Button(
        window,
        fg="red",
        font=("Calibri", 18, "italic"),
        text="Confirm",
        command=confirm_login
    ).place(x=50, y=255)

    if parent is None:
        window.mainloop()


if __name__ == "__main__":
    login()
