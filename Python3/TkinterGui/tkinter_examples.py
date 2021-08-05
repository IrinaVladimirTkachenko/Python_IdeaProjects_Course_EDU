from tkinter import *
from tkinter import font

root_window = Tk()

root_window.geometry('500x500')
root_window.title('Welcome screen')

# Create a widget (Label in this case)
hello_label = Label(root_window, text='Welcome to Tkinter!',
                    font=('arial', 20, 'bold'), fg='#12edb2', bg='#10a0bc',
                    relief='groove') # solid, flat, raised, sunken, ridge, groove
# Put the widget on the root window
hello_label.pack()

version_label = Label(root_window, text='version 8.6')
version_label.pack()

go_button = Button(root_window, text='Go!',
                   font=('arial', 20, 'bold'), fg='#12edb2',
                   highlightbackground='#10a0bc',
                   relief=RAISED)
go_button.pack()

# print(font.families())
# print(TkVersion)

root_window.mainloop()

