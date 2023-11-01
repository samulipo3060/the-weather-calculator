import tkinter as tk
from tkinter import ttk

window = tk.Tk()

# Create a Combobox
combobox = ttk.Combobox(window)
combobox.pack()

# Set the values for the Combobox
combobox['values'] = ('Option 1', 'Option 2', 'Option 3')

# Set the default value
combobox.set('Option 1')

window.mainloop()

