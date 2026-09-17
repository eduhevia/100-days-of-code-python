from tkinter import *

root = Tk()
root.geometry("225x100")
root.config(padx=15, pady=15)
root.title("Miles to Km Converter")
root.minsize(225, 100)
root.maxsize(225, 100)
root.resizable(False, False)


def calculate_action():
    miles = float(entry.get().replace(",", "."))
    if miles != 0:
        km = miles * 1.609344
        converted_label.config(text=round(km, 2))


# Labels
miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

equal_label = Label(text="is equal to")
equal_label.grid(column=0, row=1)

converted_label = Label(text="0")
converted_label.grid(column=1, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)


# Entries
entry = Entry(width=7)
entry.insert(END, string="0")
entry.bind("<Return>", calculate_action)
entry.grid(column=1, row=0)


# Buttons
calculate_button = Button(text="Calculate", command=calculate_action)
calculate_button.grid(column=1, row=2)

root.mainloop()
