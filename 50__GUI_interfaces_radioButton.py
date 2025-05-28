###############################################
### 50__GUI_interfaces_radioButton.py
###
### LISTA []
### TUPLA ()
###############################################

from tkinter import *

root=Tk()

varOpcion = IntVar() #Crea una variable especial de tkinter que puede almacenar números enteros

def imprimir():
    #print(varOpcion.get())

    if varOpcion.get()==1: #Verifica si el value= de varOpcion es 1 (primer bRadiobutton)
        etiqueta.config(text="has elegido MASCULINO") #cambia el texto de la etiqueta a "has elegido MASCULINO".
    elif varOpcion.get()==2:
        etiqueta.config(text="has elegido FEMENINO")
    else:
        etiqueta.config(text="has elegido OTRAS OPCIONES")

Label(root, text="Genero:").pack() #Crea una etiqueta con el texto "Género:" y la coloca en la ventana usando pack()

Radiobutton(root, text="MASCULINO", variable=varOpcion, value=1, command=imprimir).pack()   ##Crea el primer Radiobutton con:
                                                                                            ##text="MASCULINO": el texto que se muestra
                                                                                            ##variable=varOpcion: la variable que almacena la selección
                                                                                            ##value=1: el valor que se asigna cuando se selecciona este botón
                                                                                            ##command=imprimir: la función que se ejecuta al seleccionarlo
Radiobutton(root, text="FEMENINO", variable=varOpcion, value=2, command=imprimir).pack()
Radiobutton(root, text="OTRAS OPCIONES", variable=varOpcion, value=3, command=imprimir).pack()

etiqueta = Label(root) #Crea una etiqueta vacía que se usará para mostrar la selección del usuario.
etiqueta.pack() #Coloca la etiqueta en la ventana.

root.mainloop() #Inicia el bucle principal de la app. Esta línea hace que la ventana se mantenga abierta y responda a las interacciones del usuario