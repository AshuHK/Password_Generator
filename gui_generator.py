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

generate_button = Button(text="Generate", font=("Arial"), bg="red", fg="black", highlightbackground="red")
generate_button.grid(row=1, column=1, padx=5, pady=5)

root.mainloop()
