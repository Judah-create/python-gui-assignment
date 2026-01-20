import tkinter as tk
from tkinter import ttk, messagebox

root = tk.Tk()
root.title("Temperature Converter")
root.geometry("350x280")
root.resizable(False, False)

value = tk.StringVar()
from_unit = tk.StringVar(value="Celsius")
to_unit = tk.StringVar(value="Fahrenheit")

def convert():
    try:
        temp = float(value.get())

        if from_unit.get() == "Celsius" and to_unit.get() == "Fahrenheit":
            result = (temp * 9/5) + 32

        elif from_unit.get() == "Fahrenheit" and to_unit.get() == "Celsius":
            result = (temp - 32) * 5/9

        elif from_unit.get() == "Celsius" and to_unit.get() == "Kelvin":
            result = temp + 273

        elif from_unit.get() == "Kelvin" and to_unit.get() == "Celsius":
            result = temp - 273

        elif from_unit.get() == "Fahrenheit" and to_unit.get() == "Kelvin":
            result = (temp - 32) * 5/9 + 273

        elif from_unit.get() == "Kelvin" and to_unit.get() == "Fahrenheit":
            result = (temp - 273) * 9/5 + 32

        else:
            result = temp

        result_label.config(text="Result: " + str(round(result, 2)))

    except:
        messagebox.showerror("Error", "Enter a valid number")

tk.Label(root, text="Temperature Converter", font=("Arial", 15)).pack(pady=10)

tk.Entry(root, textvariable=value).pack(pady=5)

ttk.Combobox(root, textvariable=from_unit,
             values=["Celsius", "Fahrenheit", "Kelvin"],
             state="readonly").pack(pady=5)

ttk.Combobox(root, textvariable=to_unit,
             values=["Celsius", "Fahrenheit", "Kelvin"],
             state="readonly").pack(pady=5)

tk.Button(root, text="Convert", command=convert).pack(pady=10)

result_label = tk.Label(root, text="Result:")
result_label.pack()

root.mainloop()
