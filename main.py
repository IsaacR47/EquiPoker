import tkinter as tk
from tkinter import messagebox
import sqlite3

root = tk.Tk()
root.title("Poker Bankroll Manager")

conn = sqlite3.connect('poker_bankroll.db')
c = conn.cursor()

def on_exit():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        conn.close()
        root.destroy()

screen_width = 800
screen_height = 600
root.geometry(f"{screen_width}x{screen_height}")

label = tk.Label(root, text="Poker Bankroll Manager", font=("Arial", 24))
label.pack(pady=20)

button_exit = tk.Button(root, text="Exit", command=on_exit)
button_exit.pack()

# Main loop
root.mainloop()
