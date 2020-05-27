from tkinter import *
from tkinter import ttk
import random
import string
import pyperclip


def shuffle_string(some_str):
    pass


def generate_password():
    size_input = size_entry.get()
    if size_input.strip().isdigit():
        size = int(size_input.strip())
    else:
        size = 16

    chars = (
        string.ascii_uppercase
        + string.ascii_lowercase
        + string.digits
        + string.punctuation
    )

    chars = shuffle_string(chars) 

    new_password = ""
    while len(new_password) < size: 
        new_password += chars[random.randint(0, len(chars) - 1)]

    new_password = shuffle_string(new_password)


root = Tk()
root.title("Random Password Generator")
root.maxsize(300, 150)
root.configure(bg="white")

# label for the password
Label(root, text="Length of password: ", bg="white").grid(
    row=0, column=0, padx=5, pady=5, sticky="w"
)

# entry for the password size
size_entry = Entry(root)
size_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")

# generate button
generate_button = Button(
    text="Generate",
    font=("Arial"),
    bg="red",
    fg="black",
    highlightbackground="red",
    command=generate_password,
)
generate_button.place(relx=0.5, rely=0.7, anchor=CENTER)

# where the password goes
Label(root, text="Password: ", bg="white").grid(row=2, column=0, padx=5, pady=5)

password_dest = Entry(root)
password_dest.grid(row=2, column=1, padx=5, pady=5)

root.mainloop()
