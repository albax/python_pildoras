###############################################
### 46__GUI_interfaces_V.py
###
### LISTA []
### TUPLA ()
###############################################

from tkinter import *

raiz = Tk()

miFrame = Frame(raiz, width=1200, height=600)
miFrame.pack()

miNombre=StringVar()

cdroNombre = Entry(miFrame, textvariable=miNombre)
cdroNombre.grid(row=0, column=1, padx=10, pady=10)
cdroNombre.config(fg="red", justify="right")

cdroPass=Entry(miFrame)
cdroPass.grid(row=1, column=1, padx=10, pady=10)
cdroPass.config(show="?")

cdroApellido=Entry(miFrame)
cdroApellido.grid(row=2, column=1, padx=10, pady=10)

cdroDireccion=Entry(miFrame)
cdroDireccion.grid(row=3, column=1, padx=10, pady=10)

txtComment = Text(miFrame, width=16, height=5)
txtComment.grid(row=4, column=1, pady=10)
scrollYComentarios= Scrollbar(miFrame, command=txtComment.yview)
scrollYComentarios.grid(row=4, column=1, pady=10, sticky="nse")
txtComment.config(yscrollcommand=scrollYComentarios.set)

scrollVert=Scrollbar(miFrame, command=txtComment.yview)

nomLabel=Label(miFrame, text="Nombre:")
nomLabel.grid(row=0, column=0, sticky="e", padx=10, pady=10)

passLabel=Label(miFrame, text="Password:")
passLabel.grid(row=1, column=0, sticky="e", padx=10, pady=10)

apeLabel=Label(miFrame, text="Apellido:")
apeLabel.grid(row=2, column=0, sticky="e", padx=10, pady=10)

dirLabel=Label(miFrame, text="Direccion:")
dirLabel.grid(row=3, column=0, sticky="e", padx=10, pady=10)

commentLabel=Label(miFrame, text="Comentarios:")
commentLabel.grid(row=4, column=0, sticky="e", padx=10, pady=10)


def codigoBton():
    miNombre.set("Alberto")
    
btonEnvio=Button(raiz, text="Enviar", command=codigoBton)    
btonEnvio.pack()

raiz.mainloop()
