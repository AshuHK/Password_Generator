from tkinter import * 
from tkinter import ttk 
import random 
import pyperclip

root = Tk() 
root.title("Random Password Generator")
root.maxsize(300, 150) 
root.configure(bg="white") 

# label for the password 
Label(root, text="Length of password: ", bg="white").grid(row=0, column=0, padx=5, pady=5, sticky="w")

# entry for the password size
size_entry = Entry(root) 
size_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")

# generate button 
generate_button = Button(text="Generate", font=("Arial"), bg="red", fg="black", highlightbackground="red")
generate_button.grid(row=1, column=1, padx=5, pady=5)

# where the password goes 
Label(root, text="Password: ", bg="white").grid(row=2, column=0, padx=5, pady=5)

password_dest = Entry(root)
password_dest.grid(row=2, column=1, padx=5, pady=5)

root.mainloop()
