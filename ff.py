import tkinter as tk
from tkinter import messagebox

window = (link unavailable)()
window.title("Registration Form")

def submit_form():
    name = name_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if name == "" or email == "" or password == "":
        messagebox.showerror("Error", "Please fill in all fields")
    else:
        print("Name:", name)
        print("Email:", email)
        print("Password:", password)

        messagebox.showinfo("Success", "Registration successful")

name_label = tk.Label(window, text="Name:")
name_label.pack()
name_entry = tk.Entry(window)
name_entry.pack()
email_label = tk.Label(window, text="Email:")
email_label.pack()
email_entry = tk.Entry(window)
email_entry.pack()

password_label = tk.Label(window, text="Password:")
password_label.pack()
password_entry = tk.Entry(window, show="*")
password_entry.pack()
