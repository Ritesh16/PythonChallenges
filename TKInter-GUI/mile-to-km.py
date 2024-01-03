from tkinter import *

def miles_to_km():
    miles = float(miles_input.get())
    km = round(miles * 1.609)
    km_convert_label.config(text=f"{km}")

window = Tk()
window.title("Mile to KM converter")
window.config(padx=20, pady=20)

miles_input = Entry(width=10)
miles_input.grid(row=0, column=1)

miles_label = Label(text="Miles")
miles_label.grid(row=0, column=2)

is_equal_to_label = Label(text="is equal to")
is_equal_to_label.grid(row=1, column=0)

km_convert_label = Label(text="0")
km_convert_label.grid(row=1, column=1)

km_label = Label(text="KM")
km_label.grid(row=1, column=2)

button = Button(text="Calculate", command=miles_to_km)
button.grid(row=2, column=1)

window.mainloop()
