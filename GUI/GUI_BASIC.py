from tkinter import *

GUI = Tk()
GUI.title('My app')
GUI.geometry('500x400')

L1 = Label(GUI, text='Header')
L1.pack()

E1 = Entry(GUI)
E1.pack()

L2 = Label(GUI, text='Note')
L2.pack()

E2 = Entry(GUI)
E2.pack()

B1 = Button(GUI, text='Save')
B1.pack()

GUI.mainloop()