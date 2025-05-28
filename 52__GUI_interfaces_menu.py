###############################################
### 52__GUI_interfaces_menu.py
###
### LISTA []
### TUPLA ()
###############################################

from tkinter import *

root=Tk() #Crea la ventana principal de la aplicación.

barraMenu = Menu(root) #Crea la barra de menú principal que contendrá todos los menús desplegables.
root.config(menu=barraMenu, width=300, height=300) 
""" Configura la ventana para que:
    menu=barraMenu: Use la barra de menú creada
    width=300, height=300: Tenga un tamaño de 300x300 píxeles
""" 

archivoMenu=Menu(barraMenu, tearoff=0)
""" Crea el menú "Archivo" con:
        barraMenu: Como menú padre
        tearoff=0: Impide que el menú se pueda "desprender" de la barra (característica de algunos sistemas)
""" 
#archivoMenu.add_command(label="Nuevo") #Añade opciones al menú Archivo. Cada add_command() crea una opción clickeable con el texto especificado.

def nuevo_archivo():
    print("Nuevo archivo creado")

def guardar_archivo():
    print("Archivo guardado")

archivoMenu.add_command(label="Nuevo", command=nuevo_archivo)
archivoMenu.add_command(label="Guardar", command=guardar_archivo)

#archivoMenu.add_command(label="Guardar")
archivoMenu.add_command(label="Guardar como")
archivoMenu.add_separator() #Añade una línea separadora visual entre las opciones del menú.
archivoMenu.add_command(label="Cerrar")
archivoMenu.add_command(label="Salir")

archivoEdicion=Menu(barraMenu, tearoff=0)
archivoEdicion.add_command(label="Copiar")
archivoEdicion.add_command(label="Cortar")
archivoEdicion.add_command(label="Pegar")

archivoHerramientas=Menu(barraMenu)

archivoAyuda=Menu(barraMenu, tearoff=0)
archivoAyuda.add_command(label="Licencia")
archivoAyuda.add_command(label="Acerca de...")

barraMenu.add_cascade(label="Archivo", menu=archivoMenu)
""" Añade todos los menús a la barra principal. add_cascade() crea los elementos principales que se ven en la barra de menú:
        label: El texto que aparece en la barra
        menu: El menú desplegable asociado
""" 
barraMenu.add_cascade(label="Edicion", menu=archivoEdicion)
barraMenu.add_cascade(label="Herramientas", menu=archivoHerramientas)
barraMenu.add_cascade(label="Ayuda", menu=archivoAyuda)

root.mainloop() #Inicia el bucle principal de la app. Esta línea hace que la ventana se mantenga abierta y responda a las interacciones del usuario