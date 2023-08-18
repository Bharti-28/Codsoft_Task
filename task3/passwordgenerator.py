import random
import string
import tkinter as tk
from tkinter import messagebox


def generatePassword(length, complexity):
    characters = string.ascii_letters + string.digits
    if complexity == "high":
        characters += string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generatePassword_button_click():
    name = name_entry.get().strip()
    length = int(length_entry.get())
    complexity = complexity_var.get()

    if name == "":
        messagebox.showerror("Error", "Please enter your name.")
        return

    password = generatePassword(length, complexity)
    result_label.config(text=f"Your password is: {password}")
    accept_button.config(state=tk.NORMAL)
    reject_button.config(state=tk.NORMAL)

def accept_password():
    messagebox.showinfo("Accepted", "Password accepted")

def reject_password():
    result_label.config(text="")
    accept_button.config(state=tk.DISABLED)
    reject_button.config(state=tk.DISABLED)

window = tk.Tk()
window.configure(bg="lightgray")
window.title("Password Generator")

heading_label = tk.Label(window, text="Password Generator", font=("sens-serif", 18, "bold"),bg="lightgray")
heading_label.grid(pady=10, column=1, columnspan=10)
    
name_label = tk.Label(window, text="Name:", font=("Helvetica", 12), bg="lightgray")
name_label.grid(row=1, column=1, padx=10, pady=15, sticky="e")

name_entry = tk.Entry(window, width=30)
name_entry.grid(row=1, column=2, padx=10, pady=15)

length_label = tk.Label(window, text="Password Length:", font=("Helvetica", 12), bg="lightgray")
length_label.grid(row=2, column=1, padx=10, pady=15, sticky="e")

length_entry = tk.Entry(window, width=30)
length_entry.grid(row=2, column=2, padx=10, pady=15)

complexity_label = tk.Label(window, text="Complexity Level:", font=("Helvetica", 12), bg="lightgray")
complexity_label.grid(row=3, column=1, padx=10, pady=15, sticky="e")

complexity_var = tk.StringVar()
complexity_var.set("low")

complexity_radio_low = tk.Radiobutton(window, text="Low", variable=complexity_var, value="low", bg="lightgray")
complexity_radio_low.grid(row=3, column=2, padx=10, pady=15, sticky="w")

complexity_radio_high = tk.Radiobutton(window, text="High", variable=complexity_var, value="high", bg="lightgray")
complexity_radio_high.grid(row=4, column=2, padx=10, pady=15, sticky="w")

generatePassword_button = tk.Button(window, text="Generate password", command=generatePassword_button_click, font=("Helvetica", 12), bg="lightgray", relief="groove" )
generatePassword_button.grid(row=5, column=1, columnspan=19, padx=10, pady=10)

result_label = tk.Label(window, text="", wraplength=400, bg="lightgray", font=("Helvetica", 12))
result_label.grid(row=6, column=1, columnspan=2, padx=10, pady=15)

accept_button = tk.Button(window, text="Accept", state=tk.DISABLED, command=accept_password, bg="gainsboro", relief="groove")
accept_button.grid(row=7, column=1, padx=70, pady=25)

reject_button = tk.Button(window, text="Reject", state=tk.DISABLED, command=reject_password, bg="orangered", relief="groove")
reject_button.grid(row=7, column=2, padx=10, pady=25)

window.mainloop()