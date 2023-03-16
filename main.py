from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"

# -------------------------- PROGRAM START -------------------------- #
# Reading data
try:  # Read from user's saved data
    word_file = pd.read_csv('data/words_to_learn.csv', encoding='latin1')
except FileNotFoundError:  # If not found read the main original data
    word_file = pd.read_csv('data/german_words.csv', encoding='latin1')

# converting csv data to a list of dicts
words_to_learn = word_file.to_dict(orient="records")
current_word = {}

# -------------------------- MAIN FUNCTIONS ------------------------ #


def remove_word():  # remove the word from the learning list and create\rewrite 'words_to_learn' file
    global words_to_learn
    words_to_learn.remove(current_word)
    df = pd.DataFrame(words_to_learn)
    df.to_csv('data/words_to_learn.csv', encoding='latin1', index=False)
    generate_word()


def generate_word():  # View a random german word from the dataset and wait 5 seconds before flipping
    global current_word, timer
    window.after_cancel(timer)
    current_word = random.choice(words_to_learn)
    canvas.itemconfig(canvas_image, image=front_image)
    canvas.itemconfig(canvas_word, fill='black', text=current_word['German'])
    canvas.itemconfig(canvas_title, fill='black', text="German")
    timer = window.after(5000, func=flip_card)


def flip_card():  # View the English translation
    canvas.itemconfig(canvas_image, image=back_image)
    canvas.itemconfig(canvas_word, fill='white', text=f"{current_word['English']}")
    canvas.itemconfig(canvas_title, fill='white', text="English")


# ----------------------------- UI ---------------------------- #

# Main window layout
window = Tk()
window.title("German Vocab Learning App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
# Setting a 5 seconds wait before flipping card
timer = window.after(5000, func=flip_card)
# Background Image
canvas = Canvas(width=800, height=526)
front_image = PhotoImage(file='images/card_front.png')
back_image = PhotoImage(file='images/card_back.png')
canvas_image = canvas.create_image(400, 263, image=front_image)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)
# Text on Screen
canvas_title = canvas.create_text(400, 150, text="", font=('Ariel', 40, 'italic'))
canvas_word = canvas.create_text(400, 263, text="", font=('Ariel', 60, 'bold'))
# Buttons
cross_image = PhotoImage(file='images/wrong.png')
unknown_button = Button(image=cross_image, highlightthickness=0, command=generate_word)
unknown_button.grid(row=1, column=0)

checkmark_image = PhotoImage(file='images/right.png')
checkmark_button = Button(image=checkmark_image, highlightthickness=0, command=remove_word)
checkmark_button.grid(row=1, column=1)

# PROGRAM LOOP
generate_word()
window.mainloop()
