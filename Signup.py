import tkinter as tk
from tkinter import messagebox

def sign_up():
    username = entry_name.get()
    email = entry_email.get()
    password = entry_password.get()
    confirm_password = entry_confirm_password.get()
    
    if not username or not email or not password or not confirm_password:
        messagebox.showerror("Error", "All fields are required!")
        return
    
    if password != confirm_password:
        messagebox.showerror("Error", "Passwords do not match!")
        return
    
    # You can replace this with actual logic to save user data
    messagebox.showinfo("Success", f"Account created successfully for {username}!")
    root.destroy()

# Create the main window
root = tk.Tk()
root.title("Sign-Up Page")
root.geometry("400x400")

# Title Label
label_title = tk.Label(root, text="Sign-Up", font=("Arial", 20))
label_title.pack(pady=20)

# Name Field
label_name = tk.Label(root, text="Name:")
label_name.pack(anchor="w", padx=20)
entry_name = tk.Entry(root, width=40)
entry_name.pack(padx=20, pady=5)

# Email Field
label_email = tk.Label(root, text="Email:")
label_email.pack(anchor="w", padx=20)
entry_email = tk.Entry(root, width=40)
entry_email.pack(padx=20, pady=5)

# Password Field
label_password = tk.Label(root, text="Password:")
label_password.pack(anchor="w", padx=20)
entry_password = tk.Entry(root, show="*", width=40)
entry_password.pack(padx=20, pady=5)

# Confirm Password Field
label_confirm_password = tk.Label(root, text="Confirm Password:")
label_confirm_password.pack(anchor="w", padx=20)
entry_confirm_password = tk.Entry(root, show="*", width=40)
entry_confirm_password.pack(padx=20, pady=5)

# Sign-Up Button
btn_sign_up = tk.Button(root, text="Sign Up", command=sign_up, width=20, bg="blue", fg="white")
btn_sign_up.pack(pady=20)

# Run the application
root.mainloop()
