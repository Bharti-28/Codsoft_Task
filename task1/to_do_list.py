import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Empty Task", "Please enter some task.")

def delete_task():
    try:
        index = listbox.curselection()
        listbox.delete(index)
    except:
        messagebox.showwarning("No task selected, Please select a task to delete.")

def update_task():
    try:
        index = listbox.curselection()
        selected_task = listbox.get(index)
        updated_task = entry.get()
        if updated_task:
            listbox.delete(index)
            listbox.insert(index, updated_task)
            entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Please Enter new task")
    except:
        messagebox.showwarning("Please select a Task to update")

def clear_tasks():
    listbox.delete(0, tk.END)

root = tk.Tk()
root.title("To-Do-List")

# create Listbox
listbox = tk.Listbox(root, width=50, bg="gray", fg="black")
listbox.pack(pady=20)

# create entry box
entry = tk.Entry(root, font=("Helvetica", 12), width=30, border=2, relief="groove")
entry.pack(pady=10)

# create button
button_line = tk.Frame(root)
button_line.pack(pady=20)

add_button = tk.Button(button_line, text="Add Task", command=add_task, bg="blue", fg="white")
add_button.grid(row=0, column=0, padx=6)

delete_button = tk.Button(button_line, text="Delete Task", command=delete_task, bg="red", fg="white")
delete_button.grid(row=0, column=1, padx=6)

update_button = tk.Button(button_line, text="Update Task", command=update_task, bg="green", fg="white")
update_button.grid(row=0, column=2, padx=6)

clear_button = tk.Button(button_line, text="Clear All", command=clear_tasks, bg="black", fg="white")
clear_button.grid(row=0, column=3, padx=6)

root.mainloop()