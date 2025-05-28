###############################################
### 51__GUI_interfaces_checkButton.py
###
### LISTA []
### TUPLA ()
###############################################

from tkinter import *

root=Tk() #Crea la ventana principal de la aplicación.

root.title("checkButton") #Establece el título de la ventana que aparecerá en la barra de título como "checkButton".

playa = IntVar()
montana = IntVar()
turismoRural = IntVar() #Crea 3 variables especiales de tkinter almacenan valores (0 o 1) para cd checkbox. C/u controla el estado de una casilla de verificación.

def opcionesViaje(): #Define la función que se ejecutará cada vez que se marque o desmarque cualquier checkbox

    opcionEscogida="" #Inicializa una cadena vacía donde se acumularán las opciones seleccionadas.

    if(playa.get()==1):
        opcionEscogida+=" playa" #Verifica si el checkbox de playa está marcado (valor 1). Si es así, añade "playa" a la cadena de opciones.
    if(montana.get()==1):
        opcionEscogida+=" montana" #Si el checkbox de montaña está marcado, añade "montana" a la cadena.
    if(turismoRural.get()==1):
        opcionEscogida+=" turismoRural" #Si el checkbox de turismo rural está marcado, añade "turismoRural" a la cadena.
    
    textoFinal.config(text=opcionEscogida) #Actualiza el texto de la etiqueta textoFinal con todas las opciones seleccionadas.

foto=PhotoImage(file="avion1.png") #Carga una imagen desde el archivo "avion1.png" 
Label(root, image=foto).pack() #Crea una etiqueta que muestra la imagen y la coloca en la ventana principal.

frame=Frame(root) #Crea un contenedor (frame) que servirá para organizar los elementos siguientes.
frame.pack() #Coloca el frame en la ventana principal

Label(frame, text="Elige destinos", width=50).pack() #Crea una etiqueta con el texto "Elige destinos" dentro del frame, con un ancho de 50 caracteres.

Checkbutton(frame, text="PLAYA", variable=playa, onvalue=1, offvalue=0, command=opcionesViaje).pack() 
""" Crea el primer checkbox con:
        text="PLAYA": texto que se muestra
        variable=playa: variable que controla su estado
        onvalue=1: valor cuando está marcado
        offvalue=0: valor cuando está desmarcado
        command=opcionesViaje: función que se ejecuta al cambiar estado
"""
Checkbutton(frame, text="MONTANA", variable=montana, onvalue=1, offvalue=0, command=opcionesViaje).pack()
Checkbutton(frame, text="TURISMO RURAL", variable=turismoRural, onvalue=1, offvalue=0, command=opcionesViaje).pack()


textoFinal=Label(frame) #Crea una etiqueta vacía donde se mostrarán las opciones seleccionadas.
textoFinal.pack() #Coloca la etiqueta en el frame.

root.mainloop() #Inicia el bucle principal de la app. Esta línea hace que la ventana se mantenga abierta y responda a las interacciones del usuario