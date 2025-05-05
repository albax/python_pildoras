###############################################
### 42_GUI-I_tkinter.py
###
### LISTA []
### TUPLA ()
###############################################

from tkinter import *

raiz = Tk()
raiz.title("Ventana de pruebas")
# raiz.resizable(True, False) #width, heigth
raiz.iconbitmap("gato.ico")
# raiz.geometry("650x350")
raiz.config(bg="#197278") #raiz.config(bg="blue")

miFrame = Frame()
# miFrame.pack()
miFrame.pack(side="top", anchor="n") #side left,right,top | #anchor n,s,w,e 
miFrame.pack(fill="x") #fill x, y, both
# miFrame.pack(fill="x", expand="True") #fill x, y, both
miFrame.config(bg="#81E7AF")
miFrame.config(width="650", height="150")
miFrame.config(bd="10") #bd borde
miFrame.config(relief="sunken") #flat, groove, raised, ridge, solid, or sunken
miFrame.config(cursor="pirate") #pirate, hand2

raiz.mainloop()
