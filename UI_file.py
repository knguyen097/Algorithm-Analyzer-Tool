import tkinter as TK
from tkinter import ttk
from tkinter import messagebox
import algorithm  # Ensure algorithm.py contains generate_random_array(size)

def generateArray(size):
    try:
        size = int(size)  # Convert input size to integer
        if size <= 0:
            messagebox.showerror("Input Error", "Please enter a positive integer.")
            return []
        return algorithm.generate_random_array(size)  # Call function properly
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid integer.")
        return []

def displayArray():
    size = randArray_Size.get("1.0", TK.END).strip()  
    arrayInput = generateArray(size)  
    
    if arrayInput: 
        array.delete("1.0", TK.END)  
        array.insert(TK.END, ', '.join(map(str, arrayInput)))

def buildWindow():
    global randArray_Size, array  

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

    start_Button = TK.Button(button_Frm, text="Start!", command=window.destroy)
    start_Button.grid(column=6, row=5) 

    create_RandArray = TK.Button(button_Frm, text="Generate Random Array", command=displayArray)
    create_RandArray.grid(column=3, row=2)

    # Sorting algorithm checkboxes
    mergeSort = TK.BooleanVar(value=False)

    linSearch = TK.Checkbutton(button_Frm, text="Linear Search", variable=False)
    linSearch.grid(column=1, row=5)

    radSort = TK.Checkbutton(button_Frm, text="Radix Sort", variable=False)
    radSort.grid(column=2, row=5)

    quickSort = TK.Checkbutton(button_Frm, text="Quick Sort", variable=False)
    quickSort.grid(column=3, row=5)

    bubbSort = TK.Checkbutton(button_Frm, text="Bubble Sort", variable=False)
    bubbSort.grid(column=4, row=5)

    mergeSort = TK.Checkbutton(button_Frm, text="Merge Sort", variable=mergeSort)
    mergeSort.grid(column=5, row=5)

    # Input field for array size
    arrayPrompt = TK.Label(button_Frm, height=1, width=20, text="Input Size of Array Here:")
    arrayPrompt.grid(column=1, row=2)

    randArray_Size = TK.Text(button_Frm, height=1, width=8)
    randArray_Size.grid(column=2, row=2)

    # Text widget to display generated array
    array = TK.Text(entry_Frm, height=1, width=50, wrap="word")
    array.pack(side="left", fill="both", expand=True, padx=50, pady=100)
    
    # Scrollbar
    scrollbar = TK.Scrollbar(entry_Frm, command=array.yview)
    scrollbar.pack(side="right", fill="y")
    array.config(yscrollcommand=scrollbar.set)

    window.mainloop()

buildWindow()
