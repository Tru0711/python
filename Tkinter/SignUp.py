import tkinter as tk
from tkinter import messagebox

users = {}

def signup():
    name = entry_name.get()
    phone = entry_phone.get()
    username = entry_username.get()
    password = entry_password.get()
    
    users[username] = {
        'Name': name,
        'Phone': phone,
        'Password': password
    }
    messagebox.showinfo("Success", "Signup successful!")
    entry_name.delete(0, tk.END)
    entry_phone.delete(0, tk.END)
    entry_username.delete(0, tk.END)
    entry_password.delete(0, tk.END)

root = tk.Tk()
root.title("Signup Page")

# Set the size of the window
root.geometry("300x300")

# Name label and entry field
tk.Label(root, text="Name").grid(row=0, column=0, pady=5)
entry_name = tk.Entry(root, width=25)
entry_name.grid(row=0, column=1, pady=5)

# Phone Number label and entry field
tk.Label(root, text="Phone Number").grid(row=1, column=0, pady=5)
entry_phone = tk.Entry(root, width=25)
entry_phone.grid(row=1, column=1, pady=5)

# Username label and entry field
tk.Label(root, text="Username").grid(row=2, column=0, pady=5)
entry_username = tk.Entry(root, width=25)
entry_username.grid(row=2, column=1, pady=5)

# Password label and entry field
tk.Label(root, text="Password").grid(row=3, column=0, pady=5)
entry_password = tk.Entry(root, show="*", width=25)
entry_password.grid(row=3, column=1, pady=5)

# Signup button
tk.Button(root, text="Sign Up", command=signup).grid(row=4, columnspan=2, pady=10)

root.mainloop()
