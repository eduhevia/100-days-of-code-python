from random import choice, randint, shuffle
from tkinter import *
from tkinter import messagebox

import pyperclip

DEFAULT_EMAIL = "andreahevia12@gmail.com"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_function():
    letters = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z",
    ]
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)

    password_list = (
        [choice(letters) for _ in range(nr_letters)]
        + [choice(symbols) for _ in range(nr_symbols)]
        + [choice(numbers) for _ in range(nr_numbers)]
    )
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get().title()
    email = email_entry.get()
    password = (password_entry.get())
    if not website or not email or not password:
        messagebox.showwarning(
            title="Oops",
            message="Please don't leave any fields empty!",
        )
    else:
        if messagebox.askokcancel(
            title=website,
            message=f"These are the details entered: \nEmail: {email} \nPassword: {password}, \nIs it OK to save?",
        ):
            with open("day-29-password-manager/data/data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
root = Tk()
root.title("Password Manager")
root.config(padx=50, pady=50)

# Canvas (Logo)
canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="day-29-password-manager/data/logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1, sticky="w", pady=2)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2, sticky="w", pady=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3, sticky="w", pady=2)

# Entries
website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2, sticky="ew", pady=2)
website_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2, sticky="ew", pady=2)
email_entry.insert(0, DEFAULT_EMAIL)

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3, sticky="ew", pady=2)

# Buttons
generate_button = Button(text="Generate Password", width=14, command=generate_function)
generate_button.grid(column=2, row=3, padx=(5, 0), sticky="ew")

add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2, sticky="ew", pady=5)

root.mainloop()
