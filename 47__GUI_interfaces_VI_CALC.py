###############################################
### 47__GUI_interfaces_VI_CALC.py
###
### LISTA []
### TUPLA ()
###############################################

from tkinter import *
raiz=Tk()

miFrame = Frame(raiz)
miFrame.pack()

operacion = ""

#-------------------- PANTALLA -----------------------

nroPantalla = StringVar()

pantalla = Entry(miFrame, textvariable=nroPantalla)
pantalla.grid(row=1, column=1, padx=10, pady=10, columnspan=4)
pantalla.config(bg="black", fg="#03f943", justify="right")

#------------- PULSACIONES TECLADO --------------------

def nroPulsado(num):
    nroPantalla.set(nroPantalla.get() + num)

#---------------------- Fn SUMA -----------------------

def suma(num):
    global operacion
    global resultado
    resultado += int(num) #resultado=resultado+int(num)
    operacion = "suma"


#--------------------  FILA 1 -------------------------

bton7 = Button(miFrame, text="7", width=3, command=lambda:nroPulsado("7"))
bton7.grid(row=2, column=1)
bton8 = Button(miFrame, text="8", width=3, command=lambda:nroPulsado("8"))
bton8.grid(row=2, column=2)
bton9 = Button(miFrame, text="9", width=3, command=lambda:nroPulsado("9"))
bton9.grid(row=2, column=3)
btonDiv = Button(miFrame, text="/")
btonDiv.grid(row=2, column=4)

#--------------------  FILA 2 ------------------------

bton4 = Button(miFrame, text="4", width=3, command=lambda:nroPulsado("4"))
bton4.grid(row=3, column=1)
bton5 = Button(miFrame, text="5", width=3, command=lambda:nroPulsado("5"))
bton5.grid(row=3, column=2)
bton6 = Button(miFrame, text="6", width=3, command=lambda:nroPulsado("6"))
bton6.grid(row=3, column=3)
btonMulti = Button(miFrame, text="x", width=3)
btonMulti.grid(row=3, column=4)

#--------------------  FILA 3 ------------------------

bton1 = Button(miFrame, text="1", width=3, command=lambda:nroPulsado("1"))
bton1.grid(row=4, column=1)
bton2 = Button(miFrame, text="2", width=3, command=lambda:nroPulsado("2"))
bton2.grid(row=4, column=2)
bton3 = Button(miFrame, text="3", width=3, command=lambda:nroPulsado("3"))
bton3.grid(row=4, column=3)
btonRest = Button(miFrame, text="-", width=3)
btonRest.grid(row=4, column=4)

#--------------------  FILA 3 ------------------------

bton0 = Button(miFrame, text="0", width=3, command=lambda:nroPulsado("0"))
bton0.grid(row=5, column=1)
btonComa = Button(miFrame, text=",", width=3)
btonComa.grid(row=5, column=2)
btonIgual = Button(miFrame, text="=", width=3)
btonIgual.grid(row=5, column=3)
btonSum = Button(miFrame, text="+", width=3, command=lambda:suma())
btonSum.grid(row=5, column=4)



raiz.mainloop()
