from tkinter import *
import random
import settings


def next_turn():
    pass


def change_direction(new_direction):
    pass


def check_collisions():
    pass


def game_over():
    pass


window = Tk()
window.title("Snake Game")
window.resizable(False, False)

score = 0
direction = "down"

label = Label(window, text=f"Score: {score}", font=("consolas", 40))
label.pack()

canvas = Canvas(
    window,
    bg=settings.BACKGROUND_COLOR,
    height=settings.GAME_HEIGHT,
    width=settings.GAME_WIDTH
)
canvas.pack()
window.mainloop()
