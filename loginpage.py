
import tkinter as tk
from tkinter import messagebox

# Create the main window
window = tk.Tk()

# Set the title of the window
window.title("Login page")

window.configure(bg="lightblue")

# Set the size of the window
window.geometry("400x300")  # width x height

# Create a frame
frame = tk.Frame(window, bg='lightblue')
frame.pack(pady=50)

def login():
    username = "anusingh"
    password = "12345"
    name="anu"
    if username_entry.get()==username and password_entry.get()==password and name_entry.get()==name:
        messagebox.showinfo(title="Login Success", message="You successfully logged in.")
    else:
        messagebox.showerror(title="Error", message="Invalid login.")



# Creating widgets
login_label = tk.Label(frame, text="Login", bg='lightblue', fg="pink", font=("Arial", 30))
username_label = tk.Label(frame, text="Username", bg='lightblue', fg="#FFFFFF", font=("Arial", 16))
username_entry = tk.Entry(frame, font=("Arial", 16))

name_label = tk.Label(frame, text="Name", bg='lightblue', fg="#FFFFFF", font=("Arial", 16))
name_entry = tk.Entry(frame, font=("Arial", 16))

password_label = tk.Label(frame, text="Password", bg='lightblue', fg="#FFFFFF", font=("Arial", 16))
password_entry = tk.Entry(frame, show="*", font=("Arial", 16))

login_button = tk.Button(frame, text="Login", bg="pink", fg="#FFFFFF", font=("Arial", 16), command=login)

# Placing widgets on the frame using grid
login_label.grid(row=0, column=0, columnspan=2, pady=10)
username_label.grid(row=1, column=0, sticky="e", pady=10)
username_entry.grid(row=1, column=1, pady=10)

name_label.grid(row=2, column=0, sticky="e", pady=10)
name_entry.grid(row=2, column=1, pady=10)

password_label.grid(row=3, column=0, sticky="e", pady=10)
password_entry.grid(row=3, column=1, pady=10)

login_button.grid(row=4, column=0, columnspan=2, pady=20)

# Run the application
window.mainloop()

