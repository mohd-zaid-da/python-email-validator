import re
import tkinter as tk
from tkinter import messagebox

# Email validation function
def validate_email():
    email = entry_email.get()

    # Strong regex
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    if re.match(pattern, email):
        result_label.config(text="Valid Email ✅", fg="green")
    else:
        result_label.config(text="Invalid Email ❌", fg="red")


# GUI setup
root = tk.Tk()
root.title("Email Validator")
root.geometry("400x250")
root.resizable(False, False)

# Title
title_label = tk.Label(root, text="Email Validator", font=("Arial", 16, "bold"))
title_label.pack(pady=15)

# Email input
entry_email = tk.Entry(root, width=35, font=("Arial", 12))
entry_email.pack(pady=10)

# Validate button
validate_btn = tk.Button(root, text="Validate", command=validate_email, width=15)
validate_btn.pack(pady=10)

# Result label
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

# Run app
root.mainloop()
