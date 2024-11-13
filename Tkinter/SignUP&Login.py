import tkinter as tk
from tkinter import messagebox
import bcrypt

# Dictionary to simulate a database of users
users = {}

def hash_password(password):
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())

def check_password(hashed_password, user_password):
    return bcrypt.checkpw(user_password.encode(), hashed_password)

def open_signup():
    signup_window = tk.Toplevel(root)
    signup_window.title("Signup")

    # Signup page layout
    tk.Label(signup_window, text="Full Name").grid(row=0, column=0, padx=10, pady=10)
    full_name_entry = tk.Entry(signup_window)
    full_name_entry.grid(row=0, column=1, padx=10, pady=10)

    tk.Label(signup_window, text="Email").grid(row=1, column=0, padx=10, pady=10)
    email_entry = tk.Entry(signup_window)
    email_entry.grid(row=1, column=1, padx=10, pady=10)

    tk.Label(signup_window, text="Phone Number").grid(row=2, column=0, padx=10, pady=10)
    phone_entry = tk.Entry(signup_window)
    phone_entry.grid(row=2, column=1, padx=10, pady=10)

    tk.Label(signup_window, text="Username").grid(row=3, column=0, padx=10, pady=10)
    username_entry = tk.Entry(signup_window)
    username_entry.grid(row=3, column=1, padx=10, pady=10)

    tk.Label(signup_window, text="Password").grid(row=4, column=0, padx=10, pady=10)
    password_entry = tk.Entry(signup_window, show="*")
    password_entry.grid(row=4, column=1, padx=10, pady=10)

    tk.Label(signup_window, text="Confirm Password").grid(row=5, column=0, padx=10, pady=10)
    confirm_password_entry = tk.Entry(signup_window, show="*")
    confirm_password_entry.grid(row=5, column=1, padx=10, pady=10)

    def signup():
        full_name = full_name_entry.get()
        email = email_entry.get()
        phone = phone_entry.get()
        username = username_entry.get()
        password = password_entry.get()
        confirm_password = confirm_password_entry.get()

        if username in users:
            messagebox.showerror("Error", "Username already exists.")
        elif password != confirm_password:
            messagebox.showerror("Error", "Passwords do not match.")
        else:
            hashed_pw = hash_password(password)
            users[username] = {
                "full_name": full_name,
                "email": email,
                "phone": phone,
                "password": hashed_pw,
            }
            messagebox.showinfo("Success", "Signup successful!")
            signup_window.destroy()

    tk.Button(signup_window, text="Signup", command=signup).grid(row=6, column=0, columnspan=2, pady=10)

def open_login():
    login_window = tk.Toplevel(root)
    login_window.title("Login")

    # Login page layout
    tk.Label(login_window, text="Username").grid(row=0, column=0, padx=10, pady=10)
    username_entry = tk.Entry(login_window)
    username_entry.grid(row=0, column=1, padx=10, pady=10)

    tk.Label(login_window, text="Password").grid(row=1, column=0, padx=10, pady=10)
    password_entry = tk.Entry(login_window, show="*")
    password_entry.grid(row=1, column=1, padx=10, pady=10)

    def login():
        username = username_entry.get()
        password = password_entry.get()

        if username not in users:
            messagebox.showerror("Error", "Username does not exist.")
        else:
            if check_password(users[username]["password"], password):
                messagebox.showinfo("Success", f"Welcome, {users[username]['full_name']}!")
                login_window.destroy()
            else:
                messagebox.showerror("Error", "Incorrect password.")

    tk.Button(login_window, text="Login", command=login).grid(row=2, column=0, columnspan=2, pady=10)

# Main window setup
root = tk.Tk()
root.title("Welcome")

tk.Button(root, text="Go to Signup", command=open_signup).pack(pady=10)
tk.Button(root, text="Go to Login", command=open_login).pack(pady=10)

root.mainloop()
