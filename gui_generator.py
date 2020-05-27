from tkinter import *
from tkinter import ttk
import random
import string
import pyperclip


def shuffle_string(some_str):
    """
    Shuffle a string and return it 

    :param some_str: String where the string is shuffled 
    
    :return: String of the same characters but shuffled
    """
    char_list = list(some_str)
    random.shuffle(char_list)
    return "".join(char_list)


def update_file(password):
    """
    Update (or create if necessary) a file to store the most recent passwords 

    :param password: String of the password to add to the file
    """
    file_obj = open("passwords.txt", "a")
    file_obj.write("{}\n".format(password))
    file_obj.close()


def generate_password():
    """
    Generate and displays the randomly generated password 
    """
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
    update_file(new_password)
    pyperclip.copy(new_password)

    password_dest.delete(0, END)
    password_dest.insert(0, new_password)

    Label(root, text="Updated passwords.txt\nCopied to Clipboard :)", bg="white").place(
        relx=0.5, rely=0.6, anchor=CENTER
    )

# set up the basic parameters for the window 
root = Tk()
root.title("Random Password Generator")
root.maxsize(350, 150)
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
generate_button.place(relx=0.5, rely=0.8, anchor=CENTER)

# where the password goes
Label(root, text="Password: ", bg="white").grid(row=2, column=0, padx=5, pady=5)
password_dest = Entry(root)
password_dest.grid(row=2, column=1, padx=5, pady=5)

root.mainloop()
