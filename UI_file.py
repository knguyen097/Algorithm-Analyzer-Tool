import tkinter as TK
from tkinter import ttk
from tkinter import messagebox
import algorithm


def buildWindow():
    window = TK.Tk()
    window.geometry("793x393")
    frm = ttk.Frame(window, padding=155, borderwidth=5, relief="ridge")
    frm.grid()
    frm.grid_rowconfigure(0, weight=1)
    frm.grid_columnconfigure(0, weight=1)
    window.title("Time Complexity Evaluator")
    TK.Button(frm, text="Quit", command=window.destroy).grid(column=3, row=9)

    linSearch = TK.BooleanVar(value=False)
    radSort = TK.BooleanVar(value=False)
    quickSort = TK.BooleanVar(value=False)
    bubbSort = TK.BooleanVar(value=False)
    mergeSort = TK.BooleanVar(value=False)

    TK.Checkbutton(frm, text="Linear Search", variable=linSearch).grid(column=1, row= 5)
    TK.Checkbutton(frm, text="Radix Sort", variable=radSort).grid(column=2, row= 5)
    TK.Checkbutton(frm, text="Quick Sort", variable=quickSort).grid(column=3, row= 5)
    TK.Checkbutton(frm, text="Bubble Sort", variable=bubbSort).grid(column=4, row= 5)
    TK.Checkbutton(frm, text="Merge Sort", variable=mergeSort).grid(column=5, row= 5)

    TK.Entry(frm).grid(column=3,row=2)

    window.mainloop()

