import tkinter as tk
from tkinter.filedialog import *
import pyautogui

root = tk.Tk()

canvas = tk.Canvas(root, width=300, height=300)
canvas.pack()


def take_screenshot():
    my_screenshot = pyautogui.screenshot()
    save_as = asksaveasfilename()
    my_screenshot.save(save_as + "screenshot.png")


button_pattern = tk.Button(text="Take screenshot", command=take_screenshot, font=10)
canvas.create_window(150, 150, window=button_pattern)

root.mainloop()
