import tkinter as tk

def show_ticket():
    name = entry_name.get()
    destination = entry_dest.get()
    label_result.config(text="Name: " + name + "\nDestination: " + destination)

window = tk.Tk()
window.title("Plane Ticket")

tk.Label(window, text="Passenger Name").pack()
entry_name = tk.Entry(window)
entry_name.pack()

tk.Label(window, text="Destination").pack()
entry_dest = tk.Entry(window)
entry_dest.pack()

tk.Button(window, text="Generate Ticket", command=show_ticket).pack()

label_result = tk.Label(window, text="")
label_result.pack()

window.mainloop()
