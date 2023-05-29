#imports the tkinter and ttk modules. 
import tkinter as tk
from tkinter import ttk


# Define a function to handle the combobox selection event.
def on_select(event):
#Get the selected item from the combobox.
    selected_item = event.widget.get()
    print("selected item:", selected_item)

# Create a root window and Set the title of the root window.
root = tk.Tk()
root.title("combobox example")
#Create a list of items for the combobox
items = ["Item 1", "Item 2", "Item 3", "Item 4", "Item 5"]
# create the combo box object, put the object in the root window and populate values.
combo_box = ttk.Combobox(root, values=items)
# bind it to the on_select event 
combo_box.bind("<<Comboboxselected>>", on_select)
#pack the combobox widget into the root window.
combo_box.pack()
# start the mainloop
root.mainloop()