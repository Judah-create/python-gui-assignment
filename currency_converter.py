import tkinter as tk

def convert():
    naira = float(entry_naira.get())
    dollar = naira / 1500
    label_result.config(text="Dollar: " + str(dollar))

window = tk.Tk()
window.title("Currency Converter")

tk.Label(window, text="Amount in Naira").pack()
entry_naira = tk.Entry(window)
entry_naira.pack()

tk.Button(window, text="Convert", command=convert).pack()

label_result = tk.Label(window, text="")
label_result.pack()

window.mainloop()
