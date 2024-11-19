import tkinter as tk
from tkinter import ttk, messagebox

def register():
    # Retrieve data from input fields
    name = entry_name.get()
    email = entry_email.get()
    password = entry_password.get()
    gender = gender_var.get()
    country = country_var.get()
    
    if not name or not email or not password or gender == "Select" or country == "Select":
        messagebox.showerror("Error", "All fields are required!")
        return

    # Replace this section with your logic to save user data
    messagebox.showinfo("Success", f"Registration successful for {name}!")
    root.destroy()

# Create the main window
root = tk.Tk()
root.title("Registration Page")
root.geometry("400x500")

# Title
label_title = tk.Label(root, text="Registration Form", font=("Arial", 20))
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

# Gender Radio Buttons
label_gender = tk.Label(root, text="Gender:")
label_gender.pack(anchor="w", padx=20)
gender_var = tk.StringVar(value="Select")
frame_gender = tk.Frame(root)
frame_gender.pack(anchor="w", padx=20)
tk.Radiobutton(frame_gender, text="Male", variable=gender_var, value="Male").pack(side="left")
tk.Radiobutton(frame_gender, text="Female", variable=gender_var, value="Female").pack(side="left")
tk.Radiobutton(frame_gender, text="Other", variable=gender_var, value="Other").pack(side="left")

# Country Dropdown
label_country = tk.Label(root, text="Country:")
label_country.pack(anchor="w", padx=20)
country_var = tk.StringVar(value="Select")
countries = ["India", "USA", "UK", "Canada", "Australia"]
dropdown_country = ttk.Combobox(root, textvariable=country_var, values=countries, state="readonly", width=37)
dropdown_country.pack(padx=20, pady=5)

# Register Button
btn_register = tk.Button(root, text="Register", command=register, width=20, bg="green", fg="white")
btn_register.pack(pady=30)

# Run the application
root.mainloop()
