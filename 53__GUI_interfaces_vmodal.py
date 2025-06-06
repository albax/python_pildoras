###############################################
### 53__GUI_interfaces_vmodal.py
###
### LISTA []
### TUPLA ()
###############################################

from tkinter import *
from tkinter import filedialog

root=Tk() 

def abreFichero():
    fichero=filedialog.askopenfilename(title="Abrir", initialdir="C:" filetypes=(("Excel archivos"),"*.xlsx"))
    print(fichero)

Button(root, text="Abrir fichero", command=abreFichero).pack()

root.mainloop() 