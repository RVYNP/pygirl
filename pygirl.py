import tkinter as tk
from tkinter import ttk 


def convert():
    print(entryint.get())


# window
window = tk.Tk()
window.title('demo')
window.geometry('300x150')

#title
title_label = ttk.Label(master = window, text = 'Miles to kilometers', font =('Helevetica'))
title_label.pack()

#input feild
input_frame = ttk.Frame(master = window)
entry_int = tk.IntVar()
entry = ttk.Entry(master = input_frame, textvariable= entry_int)
button = ttk.Button(master = input_frame, text = 'Convert' , command = convert)
entry.pack(side = 'left' , padx = 10)
button.pack(side = 'left')
input_frame.pack(pady = 10)


#output
output_string = tk.StringVar()
output_label = ttk.Label(master = window, text = "Output", font = 'Helvetica')
output_label.pack(pady = 5)

#run

window.mainloop()
