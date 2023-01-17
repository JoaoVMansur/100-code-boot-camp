from tkinter import *
import pandas as pd
import random
BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn ={}
try:

    data = pd.read_csv("day 31\data\wods_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("day 31\data\korean_to_english.csv")
    to_learn = original_data.to_dict(orient="records")
else:

    to_learn = data.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="Korean", fill="black")
    canvas.itemconfig(card_word, text=current_card["Korean"], fill="black")
    canvas.itemconfig(card_background, image=front_card)
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    
    canvas.itemconfig(card_background, image=back_card)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")

def is_known():
    
    
    to_learn.remove(current_card)
    print(len(to_learn))
    data = pd.DataFrame(to_learn)
    data.to_csv("day 31/data/word_to_learn.csv", index= False)
    next_card()




window = Tk()
window.title("Korean Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)
canvas = Canvas(width=800, height=526)
front_card = PhotoImage(file="day 31/images/card_front.png")
card_background = canvas.create_image(400, 263, image=front_card)
card_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)



back_card = PhotoImage(file="day 31/images/card_back.png")


right_image = PhotoImage(file="day 31/images/right.png")
wrong_image = PhotoImage(file="day 31/images/wrong.png")


right_button = Button(image=right_image, highlightthickness=0, command=is_known)
right_button.grid(column=1, row=1)
wrong_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
wrong_button.grid(column=0, row=1)

next_card()
window.mainloop()