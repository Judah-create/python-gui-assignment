import tkinter as tk
from tkinter import ttk, messagebox

routes = {
    "Ibadan": 300,
    "Ilorin": 350,
    "Akure": 320,
    "Benin": 400,
    "Owerri": 450
}

class_price = {
    "Economy": 1,
    "Business": 1.5,
    "First Class": 2
}

root = tk.Tk()
root.title("Plane Ticket System")
root.geometry("400x350")

from_city = tk.StringVar()
to_city = tk.StringVar()
travel_class = tk.StringVar(value="Economy")

def calculate_price():
    try:
        base_price = routes[from_city.get()] + routes[to_city.get()]
        total = base_price * class_price[travel_class.get()]
        messagebox.showinfo("Ticket Price", f"Total Price: ₦{total}")
    except:
        messagebox.showerror("Error", "Please select all options")

tk.Label(root, text="From").pack(pady=5)
ttk.Combobox(root, textvariable=from_city, values=list(routes.keys())).pack()

tk.Label(root, text="To").pack(pady=5)
ttk.Combobox(root, textvariable=to_city, values=list(routes.keys())).pack()

tk.Label(root, text="Class").pack(pady=5)
ttk.Combobox(
    root,
    textvariable=travel_class,
    values=["Economy", "Business", "First Class"]
).pack()

tk.Button(root, text="Calculate Ticket", command=calculate_price).pack(pady=20)

root.mainloop()
