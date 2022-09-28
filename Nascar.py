from tkinter import *
from tkinter import ttk

#Creating the background layout
GUI = Tk()
GUI.title("NASCAR Database")
GUI.geometry("900x600")
GUI.config(bg='yellow')

mainframe = Frame(GUI, height = 2040, width = 2000)
mainframe.pack_propagate(0)
mainframe.config(bg='black')
mainframe.pack(padx = 5, pady = 5)


#Title creation
Title = Label(mainframe, text = """NASCAR Database""",fg='white',bg='black')
Title.config(font=('Gill Sans', 24))
Title.pack(side = TOP)

#Exit button
menubar = Menu(GUI)
GUI.config(menu=menubar)

file_menu = Menu(menubar, tearoff=0)

file_menu.add_command(label='Are you sure?', command=GUI.destroy)
menubar.add_cascade(label="Exit", menu=file_menu)

#Menu Buttons
driver = Button(mainframe, text = """Drivers""", font=('Gill Sans', 20), padx=80, pady=20)
driver.pack()

schedule = Button(mainframe, text= """Season Schedule""", font=('Gill Sans', 20), padx=50, pady=20)
schedule.pack()

standings = Button(mainframe, text= """Season Standings""", font=('Gill Sans', 20), padx=48, pady=20)
standings.pack()

GUI.mainloop()

