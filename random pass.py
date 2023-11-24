import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_button_clicked():
    try:
        length = int(length_entry.get())
        if length <= 0:
            messagebox.showerror("Error", "Password length must be a positive integer.")
        else:
            password = generate_password(length)
            password_label.config(text="Generated Password: " + password)
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter a valid positive integer for password length.")

# Create a GUI window
root = tk.Tk()
root.title("Random Password Generator")

# Create GUI components
length_label = tk.Label(root, text="Enter Password Length:")
length_entry = tk.Entry(root)
generate_button = tk.Button(root, text="Generate Password", command=generate_button_clicked)
password_label = tk.Label(root, text="Generated Password:")

# Place components using grid layout
length_label.grid(row=0, column=0, padx=10, pady=10)
length_entry.grid(row=0, column=1, padx=10, pady=10)
generate_button.grid(row=1, columnspan=2, padx=10, pady=10)
password_label.grid(row=2, columnspan=2, padx=10, pady=10)

# Start the GUI event loop
root.mainloop()


