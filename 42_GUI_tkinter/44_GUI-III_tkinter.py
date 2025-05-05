###############################################
### 44_GUI-III_tkinter.py
###
### LISTA []
### TUPLA ()
###############################################

from tkinter import *

root = Tk()
miFrame = Frame(root, width=500, height=400)
miFrame.pack()
# miLabel = Label(miFrame, text="Hola a PYTHON")
# miLabel.place(x=100, y=200)
# Label(miFrame, text="Hola a PYTHON").place(x=100, y=200)
Label(miFrame, text="Hola a PYTHON", fg="blue", font=("Comic Sans MS", 18)).place(x=100, y=30)

miImagen = PhotoImage(file="mouse.gif")
Label(miFrame, image=miImagen).place(x=100,y=80)

root.mainloop()
