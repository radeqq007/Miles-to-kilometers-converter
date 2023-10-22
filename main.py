import tkinter as tk
from tkinter import ttk

def convert():
    output_string.set(entry_int.get()*1.61)

#window
window = tk.Tk()
window.title("Miles to kilometers converter")
window.geometry("300x150")

#title
title_label = ttk.Label(
    master = window,
    text="Miles to kilometers",
    font = "Calibri 24 bold")
title_label.pack()

#input field
input_frame = ttk.Frame(master = window)
entry_int = tk.IntVar()
entry = ttk.Entry(
    master = input_frame,
    textvariable=entry_int)

button = ttk.Button(
    master = input_frame,
    text = "convert",
    command = convert)

entry.pack(side="left", padx=5)
button.pack(side="left", padx=5)
input_frame.pack(pady=10)

#output
output_string = tk.StringVar()
output_label = ttk.Label(
    master = window,
    text="Output",
    font = "Calibri 23",
    textvariable=output_string)

output_label.pack(pady=5)

#run
window.mainloop()