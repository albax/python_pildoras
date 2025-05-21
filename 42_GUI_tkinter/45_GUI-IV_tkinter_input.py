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
cdoNombre.grid(row=0, column=1, padx=10, pady=5)
cdoNombre.config(fg="red", justify="right")

cdroPassw = Entry(miFrame)
cdroPassw.grid(row=1, column=1, padx=10, pady=5)

cdroApellido = Entry(miFrame)
cdroApellido.grid(row=2, column=1, padx=10, pady=5)

cdroDireccion = Entry(miFrame)
cdroDireccion.grid(row=3, column=1, padx=10, pady=5)

nbreLabel = Label(miFrame, text="Nombre:")
nbreLabel.grid(row=0, column=0, sticky="e", padx=10, pady=5)

apeLabel = Label(miFrame, text="Apellido:")
apeLabel.grid(row=2, column=0, sticky="e", padx=10, pady=5)

dirLabel = Label(miFrame, text="Direccion:")
dirLabel.grid(row=3, column=0, sticky="e", padx=10, pady=5)

passwLabel = Label(miFrame, text="Password:")
passwLabel.grid(row=1, column=0, sticky="e", padx=10, pady=5)


raiz.mainloop()
