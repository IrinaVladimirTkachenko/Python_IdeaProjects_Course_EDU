#from tkinter import *
#from tkinter import ttk


#def calculate(*args):
 #   try:
  #      value = float(feet.get())
   #     meters.set((0.3048 * value * 10000.0 + 0.5)/10000.0)
    #except ValueError:
     #   pass


#root = Tk()
#root.title("Feet to Meters")

#mainframe = ttk.Frame(root, padding="3 3 12 12")
#mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
#root.columnconfigure(0, weight=1)
#root.rowconfigure(0, weight=1)

#feet = StringVar()
#meters = StringVar()

#feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
#feet_entry.grid(column=2, row=1, sticky=(W, E))

#ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))
#ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)

#ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
#ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
#ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)

#for child in mainframe.winfo_children():
 #   child.grid_configure(padx=5, pady=5)

#feet_entry.focus()
#root.bind('<Return>', calculate)

#root.mainloop()

from tkinter import *
from tkinter import ttk

root = Tk()

frame = ttk.Frame(root, width=200, height=200, padding=5)
frame['borderwidth'] = 10
frame['relief'] = 'sunken'
frame.grid()

label = ttk.Label(frame, text='Full name: ')
label.grid()

resultsContents = StringVar()
label['textvariable'] = resultsContents
resultsContents.set('New value to display')

#l=ttk.Label(root, text="Starting...")
#l.grid()
#l.bind('<Enter>', lambda e: l.configure(text='Moved mouse inside'))
#l.bind('<Leave>', lambda e: l.configure(text='Moved mouse outside'))
#l.bind('<1>', lambda e: l.configure(text='Clicked left mouse button'))
#l.bind('<Double-1>', lambda e: l.configure(text='Double clicked'))
#l.bind('<B3-Motion>', lambda e: l.configure(text='right button drag to %d, %d' % (e.x, e.y)))
root.mainloop()
