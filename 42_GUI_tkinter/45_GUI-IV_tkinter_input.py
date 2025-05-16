###############################################
### 45_GUI-IV_tkinter_input.py
###
### LISTA []
### TUPLA ()
###############################################

from tkinter import *

raiz = Tk()
miFrame = Frame(raiz, width=1200, height=600)
miFrame.pack()

cdoNombre = Entry(miFrame)
cdoNombre.grid(row=0, column=1)

cdroApellido = Entry(miFrame)
cdroApellido.grid(row=1, column=1)

cdroApellido = Entry(miFrame)
cdroApellido.grid(row=1, column=1)


raiz.mainloop()
