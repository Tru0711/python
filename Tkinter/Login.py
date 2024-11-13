import tkinter as tk
from tkinter import messagebox

# Sample users data (same as in signup)
users = {
    'john_doe': {'Name': 'John Doe', 'Phone': '1234567890', 'Password': 'password123'}
}

def login():
    username = entry_username.get()
    password = entry_password.get()

    if username in users and users[username]['Password'] == password:
        messagebox.showinfo("Success", "Login successful!")
    else:
        messagebox.showerror("Error", "Invalid username or password.")

    entry_username.delete(0, tk.END)
    entry_password.delete(0, tk.END)

root = tk.Tk()
root.title("Login Page")

# Set the size of the window
root.geometry("300x200")

# Username label and entry field
tk.Label(root, text="Username").grid(row=0, column=0, pady=5)
entry_username = tk.Entry(root, width=25)
entry_username.grid(row=0, column=1, pady=5)

# Password label and entry field
tk.Label(root, text="Password").grid(row=1, column=0, pady=5)
entry_password = tk.Entry(root, show="*", width=25)
entry_password.grid(row=1, column=1, pady=5)

# Login button
tk.Button(root, text="Login", command=login).grid(row=2, columnspan=2, pady=10)

root.mainloop()
