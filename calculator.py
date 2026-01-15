import tkinter as tk

def calculate():
    a = int(entry1.get())
    b = int(entry2.get())
    label_result.config(text="Sum: " + str(a + b))

window = tk.Tk()
window.title("Calculator")

tk.Label(window, text="First Number").pack()
entry1 = tk.Entry(window)
entry1.pack()

tk.Label(window, text="Second Number").pack()
entry2 = tk.Entry(window)
entry2.pack()

tk.Button(window, text="Add", command=calculate).pack()

label_result = tk.Label(window, text="")
label_result.pack()

window.mainloop()
