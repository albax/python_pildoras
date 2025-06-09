###############################################
### 59__BBDD__practica_CRUD.py
###
### LISTA []
### TUPLA ()
###############################################
### 1. FRAMES
### 1.1. crear menu
### 1.2. crear campos (input|btons|)
### 1.3. crear BDs
### 1.4. 
### 2. BDS
### 2.1. 
### 2.2. 
###############################################

from tkinter import *
from tkinter import messagebox
import sqlite3

root=Tk() 

###--------------  1. crear menu -------------------------------
barraMenu = Menu(root) 
root.config(menu=barraMenu, width=300, height=300) 

bbddMenu=Menu(barraMenu, tearoff=0)
bbddMenu.add_command(label="Conectar")
bbddMenu.add_command(label="Salir")

borrarMenu=Menu(barraMenu, tearoff=0)
borrarMenu.add_command(label="Limpiar campos")

crudMenu=Menu(barraMenu, tearoff=0)
crudMenu.add_command(label="Crear")
crudMenu.add_command(label="Leer")
crudMenu.add_command(label="Actualizar")
crudMenu.add_command(label="Borrar")

ayudaMenu=Menu(barraMenu, tearoff=0)
ayudaMenu.add_command(label="Licencia")
ayudaMenu.add_command(label="Acerca de ...")

#agregar al Menu
barraMenu.add_cascade(label="BBDD", menu=bbddMenu)
barraMenu.add_cascade(label="Borrar", menu=borrarMenu)
barraMenu.add_cascade(label="CRUD", menu=crudMenu)
barraMenu.add_cascade(label="Ayuda", menu=ayudaMenu)

###-------------- 2. crear campos (input|btons|) ----------------------
miFrame=Frame(root)
miFrame.pack()

cuadroID=Entry(miFrame)
cuadroID.grid(row=0, column=1, padx=10, pady=10)

cuadroNombre=Entry(miFrame)
cuadroNombre.grid(row=1, column=1, padx=10, pady=10)
cuadroNombre.config(fg="red", justify="right")

cuadroPass=Entry(miFrame)
cuadroPass.grid(row=2, column=1, padx=10, pady=10)
cuadroPass.config(show="?")

cuadroApellido=Entry(miFrame)
cuadroApellido.grid(row=3, column=1, padx=10, pady=10)

cuadroDireccion=Entry(miFrame)
cuadroDireccion.grid(row=4, column=1, padx=10, pady=10)

textoComentario=Text(miFrame, width=16, height=5)
textoComentario.grid(row=5, column=1, padx=10, pady=10)
scrollVert=Scrollbar(miFrame, command=textoComentario.yview)
scrollVert.grid(row=5, column=2, sticky="nsew")

textoComentario.config(yscrollcommand=scrollVert.set)

###----------------- 3. añadir labels  -------------------------------

labelID=Label(miFrame, text="Id:")
labelID.grid(row=0, column=0, sticky="e", padx=10, pady=10)

labelNombre=Label(miFrame, text="Nombre:")
labelNombre.grid(row=1, column=0, sticky="e", padx=10, pady=10)

labelPass=Label(miFrame, text="Password:")
labelPass.grid(row=2, column=0, sticky="e",  padx=10, pady=10)

labelApellido=Label(miFrame, text="Apellido:")
labelApellido.grid(row=3, column=0, sticky="e", padx=10, pady=10)

labelDireccion=Label(miFrame, text="Direccion:")
labelDireccion.grid(row=4, column=0, sticky="e",  padx=10, pady=10)

labelComentario=Label(miFrame, text="Comentarios:")
labelComentario.grid(row=5, column=0, sticky="e", padx=10, pady=10)


###----------------- 4. añadir frame botones -------------------------------

miFrame2=Frame(root)
miFrame2.pack()

botonCrear=Button(miFrame2, text="Create")
botonCrear.grid(row=1, column=0, sticky="e", padx=10, pady=10)

botonLeer=Button(miFrame2, text="Read")
botonLeer.grid(row=1, column=1, sticky="e", padx=10, pady=10)

botonActualizar=Button(miFrame2, text="Update")
botonActualizar.grid(row=1, column=2, sticky="e", padx=10, pady=10)

botonBorrar=Button(miFrame2, text="Delete")
botonBorrar.grid(row=1, column=3, sticky="e", padx=10, pady=10)

### 2. crear BDs
#2.1. abrir|crear conexion
miConexion=sqlite3.connect("59__BBDD__practica_CRUD")

#2.2 crear puntero - cursor
miCursor=miConexion.cursor()

#2.3. executar query SQL
#### CRUD ####
#### 2.3.1. CREATE ####
# miCursor.execute('''
#     CREATE TABLE DATOSUSUARIOS(
#         ID INTEGER PRIMARY KEY AUTOINCREMENT,
#         NOM_USUARIO VARCHAR(50) UNIQUE,
#         PASSWORD VARCHAR(10),
#         APELLIDO VARCHAR(50),
#         DOCUMENTO VARCHAR(50),
#         DIRECCION VARCHAR(50),
#         EDAD INTEGER,
#         COMENTARIOS VARCHAR(100)
#     )
# ''')
## Insertar DATOS DE TABLA##
# productos = [
#     ("pelota", 20, "jugueteria"),
#     ("blusa", 10, "confeccion"),
#     ("destornillador", 40, "ferreteria"),
#     ("botya", 120, "ceramica"),
#     ("superman", 90, "jugueteria"),
#     ("robot", 50, "robotica")
# ]
# miCursor.executemany("INSERT INTO PRODUCTOS VALUES(NULL,?,?,?)", productos)

#### 2. READ ####
##"SELECT * FROM PRODUCTOS WHERE SECCION='jugueteria'"
## Aparte SOLO PARA LEER DESDE LA BD ##
# miCursor.execute("SELECT * FROM PRODUCTOS WHERE SECCION='jugueteria'")
# productos=miCursor.fetchall()
# print(productos)

#### UPDATE ####
##"SET PRECIO=366"
# miCursor.execute("UPDATE PRODUCTOS SET PRECIO=366 WHERE NOM_ARTICULO='pelota'")

#### DELETE ####
##"DELETE FROM PRODUCTOS WHERE ID=5"
# miCursor.execute("DELETE FROM PRODUCTOS WHERE ID=5")


miConexion.commit()

#5. cerrar conexion
miConexion.close()

root.mainloop()