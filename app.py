import tkinter as tk
from tkinter import ttk
import math

# Create the main window
root = tk.Tk()
root.title("Unit Converter")

# Create a dictionary to store the units and their conversion factors
units = {
    'Length': {'mm': 1, 'cm': 10, 'm': 1000, 'km': 1000000, 'in': 25.4, 'ft': 304.8, 'yd': 914.4, 'mi': 1609344},
    'Weight': {'g': 1, 'kg': 1000, 't': 1000000, 'oz': 28.35, 'lb': 453.59},
    'Volume': {'ml': 1, 'l': 1000, 'fl oz': 29.574, 'pt': 568, 'gal': 3785},
    'Temperature': {'C': 1, 'F': 1, 'K': 1}
}

# Create variables to store the user's choices
category_var = tk.StringVar()
start_unit_var = tk.StringVar()
end_unit_var = tk.StringVar()

# Function to update the unit options when the category changes
def update_units(*args):
    start_unit_combo['values'] = list(units[category_var.get()].keys())
    end_unit_combo['values'] = list(units[category_var.get()].keys())

# Function to perform the conversion
def convert():
    try:
        category = category_var.get()
        start_unit = start_unit_var.get()
        end_unit = end_unit_var.get()
        value = float(value_entry.get())

        if category == 'Temperature':
            if start_unit == 'C' and end_unit == 'F':
                result = value * 9/5 + 32
            elif start_unit == 'F' and end_unit == 'C':
                result = (value - 32) * 5/9
            elif start_unit == 'C' and end_unit == 'K':
                result = value + 273.15
            elif start_unit == 'K' and end_unit == 'C':
                result = value - 273.15
            elif start_unit == 'F' and end_unit == 'K':
                result = (value - 32) * 5/9 + 273.15
            elif start_unit == 'K' and end_unit == 'F':
                result = (value - 273.15) * 9/5 + 32
            else:
                result = value
        else:
            start_factor = units[category][start_unit]
            end_factor = units[category][end_unit]
            result = value * start_factor / end_factor

        result_label['text'] = f'{result:.2f} {end_unit}'
    except ValueError:
        result_label['text'] = 'Invalid input'
    except KeyError:
        result_label['text'] = 'Please select a category and units'

# Function to clear the entries and result
def clear():
    category_var.set('')
    start_unit_var.set('')
    end_unit_var.set('')
    value_entry.delete(0, tk.END)
    result_label['text'] = ''

# Create the category combo box
category_label = ttk.Label(root, text="Category:")
category_label.pack()
category_combo = ttk.Combobox(root, textvariable=category_var)
category_combo['values'] = list(units.keys())
category_combo.bind('<<ComboboxSelected>>', update_units)
category_combo.pack()

# Create the start unit combo box
start_unit_label = ttk.Label(root, text="Start Unit:")
start_unit_label.pack()
start_unit_combo = ttk.Combobox(root, textvariable=start_unit_var)
start_unit_combo.pack()

# Create the end unit combo box
end_unit_label = ttk.Label(root, text="End Unit:")
end_unit_label.pack()
end_unit_combo = ttk.Combobox(root, textvariable=end_unit_var)
end_unit_combo.pack()

# Create an entry for the value to convert
value_label = ttk.Label(root, text="Value:")
value_label.pack()
value_entry = ttk.Entry(root)
value_entry.pack()

# Create a button to perform the conversion
convert_button = ttk.Button(root, text="Convert", command=convert)
convert_button.pack()

# Create a button to clear the entries and result
clear_button = ttk.Button(root, text="Clear", command=clear)
clear_button.pack()

# Create a label to display the result
result_label = ttk.Label(root, text="")
result_label.pack()

# Start the main loop
root.mainloop()