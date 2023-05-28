# import tkinter library
import tkinter as tk

#  define a function that is exucuted when button is clicked.
def button_click():
    print("Button clicked!")
    
#Create the parent window of the application.
root = tk.Tk()
root.title("Button Example")

# create the button object and assign the button_click() function as the command. 
button = tk.Button(root,text="Click Me!", command=button_click)
button.pack()

# start the event loop to run the application.
root.mainloop()
