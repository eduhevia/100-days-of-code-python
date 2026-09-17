import random
import tkinter as tk

import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"
SECONDS_DELAY = 5

current_card = {}
to_learn = {}

# ---------------------------- FUNCTIONALITY ------------------------------- #
try:
    data = pd.read_csv("day-31-flash-card-project/data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("day-31-flash-card-project/data/english_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    root.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="English", fill="black")
    canvas.itemconfig(card_word, text=current_card["English"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = root.after(ms=SECONDS_DELAY * 1000, func=flip_card)


def is_known():
    to_learn.remove(current_card)
    data = pd.DataFrame(to_learn)
    data.to_csv("day-31-flash-card-project/data/words_to_learn.csv", index=False)
    next_card()


def flip_card():
    canvas.itemconfig(card_background, image=card_back_img)
    canvas.itemconfig(card_title, text="Español", fill="white")
    canvas.itemconfig(card_word, text=current_card["Español"], fill="white")


# ---------------------------- UI SETUP ------------------------------- #
root = tk.Tk()
root.title("Flashy")
root.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = root.after(SECONDS_DELAY * 1000, func=flip_card)


canvas = tk.Canvas(
    root, width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR
)
right_img = tk.PhotoImage(file="day-31-flash-card-project/images/right.png")
wrong_img = tk.PhotoImage(file="day-31-flash-card-project/images/wrong.png")

card_back_img = tk.PhotoImage(file="day-31-flash-card-project/images/card_back.png")
card_front_img = tk.PhotoImage(file="day-31-flash-card-project/images/card_front.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
canvas.grid(column=0, columnspan=2, row=0)


card_title = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))


# Buttons
known_button = tk.Button(
    image=right_img,
    highlightthickness=0,
    bg=BACKGROUND_COLOR,
    bd=0,
    activebackground=BACKGROUND_COLOR,
    command=is_known,
)
known_button.grid(column=1, row=1)

unknown_button = tk.Button(
    image=wrong_img,
    highlightthickness=0,
    bg=BACKGROUND_COLOR,
    bd=0,
    activebackground=BACKGROUND_COLOR,
    command=next_card,
)
unknown_button.grid(column=0, row=1)

next_card()

root.mainloop()
