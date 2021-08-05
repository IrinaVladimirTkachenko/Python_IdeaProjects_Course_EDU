from tkinter import *

# 1.Put a widget inside a container and have it fill the container
# 2. Put a number of widgest in a column
# 3. Put a number of widgets in a row

main_window = Tk()
#main_window.geometry('800x600+50+50')

#my_label = Label(main_window, text='My text', bg='green', fg='white')
#my_label.pack(fill=X)
#my_label.pack(fill=Y, expand=1)
#my_label.pack(fill=BOTH, expand=1)



#red_label = Label(main_window, text='Red', bg='red', fg='white')
#red_label.pack(fill=BOTH, expand=1)
#yellow_label = Label(main_window, text='Yellow', bg='yellow', fg='black')
#yellow_label.pack(fill=BOTH, expand=1)
#green_label = Label(main_window, text='Green', bg='green', fg='white')
#green_label.pack(fill=BOTH, expand=1)

#listbox = Listbox(main_window)
#listbox.pack(fill=BOTH, expand=1)

#for i in range(20):
 #   listbox.insert(END, str(i))

#red_label = Label(main_window, text='Red', bg='red', fg='white')
#red_label.pack(fill=BOTH, expand=1, padx=10)
#yellow_label = Label(main_window, text='Yellow', bg='yellow', fg='black')
#yellow_label.pack(fill=BOTH, expand=1, pady=10)
#green_label = Label(main_window, text='Green', bg='green', fg='white')
#green_label.pack(fill=BOTH, expand=1, padx=10, pady=10)

#red_label = Label(main_window, text='Red', bg='red', fg='white')
#red_label.pack(ipadx=30)
#yellow_label = Label(main_window, text='Yellow', bg='yellow', fg='black')
#yellow_label.pack(ipady=30)
#green_label = Label(main_window, text='Green', bg='green', fg='white')
#green_label.pack()

#red_label = Label(main_window, text='Red', bg='red', fg='white')
#red_label.pack(ipadx=30, side=LEFT)
#yellow_label = Label(main_window, text='Yellow', bg='yellow', fg='black')
#yellow_label.pack(ipady=30, side=LEFT)
#green_label = Label(main_window, text='Green', bg='green', fg='white')
#green_label.pack(side=LEFT)

red_label = Label(main_window, text='Red', bg='red', fg='white')
red_label.pack(ipadx=30, side=RIGHT)
yellow_label = Label(main_window, text='Yellow', bg='yellow', fg='black')
yellow_label.pack(ipady=30, side=RIGHT)
green_label = Label(main_window, text='Green', bg='green', fg='white')
green_label.pack(side=RIGHT)


main_window.mainloop()


