import tkinter as tk
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 0.1
SHORT_BREAK_MIN = 0.05
LONG_BREAK_MIN = 0.2
reps = 0
tomatos = ""
timer = None


# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title.config(text="Timer", fg=GREEN)
    global tomatos
    tomatos = ""
    status_label.config(text=tomatos)
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    global tomatos
    reps += 1
    if reps < 9:
        if reps % 8 == 0:
            title.config(text="Break", fg=RED)
            count_down(60 * LONG_BREAK_MIN)
            status_label.config(text="Well Done")
            tomatos += "✔"
            status_label.config(text=tomatos)

        if reps % 2 == 0:
            title.config(text="Break", fg=PINK)
            count_down(60 * SHORT_BREAK_MIN)
            tomatos += "✔"
            status_label.config(text=tomatos)

        else:
            title.config(text="Working", fg=GREEN)
            count_down(60 * WORK_MIN)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def count_down(count):
    mm = math.floor(count / 60)
    ss = int(count % 60)
    if ss < 10:
        ss = f"0{ss}"
    if mm < 10:
        mm = f"0{mm}"
    canvas.itemconfig(timer_text, text=f"{mm}:{ss}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    if count == 0:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #


window = tk.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
window.after(1000)
tomato_img = tk.PhotoImage(file="tomato.png")

canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

title = tk.Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
title.grid(column=1, row=0)

start_button = tk.Button(text="Start", highlightbackground=YELLOW, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = tk.Button(text="Reset", highlightbackground=YELLOW, command=reset_timer)
reset_button.grid(column=2, row=2)

status_label = tk.Label(text="", fg=RED, bg=YELLOW)
status_label.grid(column=1, row=2)

start_timer()
window.mainloop()
