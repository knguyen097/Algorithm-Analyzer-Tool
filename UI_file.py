import tkinter as TK
from tkinter import ttk
from tkinter import messagebox
import algorithm


def buildWindow():
    window = TK.Tk()
    window.geometry("793x393")
    window.title("Time Complexity Evaluator")
    # Framing for entry fields 

    entry_Frm = ttk.Frame(window)
    entry_Frm.pack(fill="both", expand=True, padx=5, pady=5)

    # Framing for buttons
    button_Frm = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")

    button_Frm.pack()
    
    
    
    # Buttons of GUI

    quit_Button = TK.Button(button_Frm, text="Quit", command=window.destroy)
    quit_Button.grid(column=3, row=9)
    start_Button = TK.Button(button_Frm, text="Start!",command=window.destroy)
    start_Button.grid(column=6, row=5) 
    create_RandArray = TK.Button(button_Frm,text= "Generate Random Array", command=window.destroy)
    create_RandArray.grid(column=3,row=2)
    
    # window.destroy needs to change so that it starts the algorithmn checking 
    # window.destroy just to place hold 

    linSearch = TK.BooleanVar(value=False)
    radSort = TK.BooleanVar(value=False)
    quickSort = TK.BooleanVar(value=False)
    bubbSort = TK.BooleanVar(value=False)
    mergeSort = TK.BooleanVar(value=False)

    TK.Checkbutton(button_Frm, text="Linear Search", variable=linSearch).grid(column=1, row= 5)
    TK.Checkbutton(button_Frm, text="Radix Sort", variable=radSort).grid(column=2, row= 5)
    TK.Checkbutton(button_Frm, text="Quick Sort", variable=quickSort).grid(column=3, row= 5)
    TK.Checkbutton(button_Frm, text="Bubble Sort", variable=bubbSort).grid(column=4, row= 5)
    TK.Checkbutton(button_Frm, text="Merge Sort", variable=mergeSort).grid(column=5, row= 5)
    
    
    # TK.Text(frm).grid(column=3,row=2)
    array = TK.Text(entry_Frm, height=1, width=20, wrap="word")
    array.pack(side="left", fill="both", expand=True, padx=50, pady=100)
    
    # Scrollbar
    scrollbar = TK.Scrollbar(entry_Frm, command=array.yview)
    scrollbar.pack(side="right", fill="y")
    array.config(yscrollcommand=scrollbar.set)



    window.mainloop()

