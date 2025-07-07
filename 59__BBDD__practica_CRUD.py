###############################################
### 59__BBDD__practica_CRUD.py
###
### LISTA []
### TUPLA ()
###############################################
### 1. FN y crear BD
#### 1.1. abrir|crear conexion
#### 1.2 crear puntero - cursor
#### 1.3. executar query SQL
### 2. FRAMES
#### 2.1. crear menu
#### 2.2. crear campos (input|btons)
#### 2.3. crear BDs
#### 2.4. 

###############################################

###--------------  1. FN y crear BD ---------------------------------------------
### 
from tkinter import *
from tkinter import messagebox
import sqlite3



def conexionBBDD():
#### 1.1. abrir|crear conexion
    miConexion=sqlite3.connect("59__BBDD_CRUD_usuario")

##1.2 crear puntero - cursor
    miCursor=miConexion.cursor()

##1.3. executar query SQL
#### CRUD ####
    try:
        miCursor.execute('''
            CREATE TABLE DATOSUSUARIOS(
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                NOM_USUARIO VARCHAR(50) UNIQUE,
                APELLIDO VARCHAR(50),
                PASSWORD VARCHAR(10),
                --DOCUMENTO VARCHAR(50),
                DIRECCION VARCHAR(50),
                --EDAD INTEGER,
                COMENTARIOS VARCHAR(100))
        ''')

        messagebox.showinfo("BBDD", "BD creada con exito")

    except:
        messagebox.showwarning("¡ATENCION¡", "la BD ya existe")

    miConexion.commit()
    miConexion.close()

def salirAplicacion():
        valor=messagebox.askquestion("SALIR","¿Deseas salir de la aplicacion?")
        if valor=='yes':
            root.destroy()

def limpiarCampos():
     miNombre.set("")
     miId.set("")
     miApellido.set("")
     miPass.set("")
     miDireccion.set("")
     textoComentario.delete(1.0, END)

def crear():
    miConexion=sqlite3.connect("59__BBDD_CRUD_usuario")
    miCursor=miConexion.cursor()
    ##codigo con ?,?,?,? consultas parametrizadas
    ##NULL,?,?,? es para no tocar el id autoincrementado
    datos=miNombre.get(),miApellido.get(),miPass.get(),miDireccion.get(),textoComentario.get("1.0", END)
    miCursor.execute("INSERT INTO DATOSUSUARIOS VALUES(NULL,?,?,?,?,?)",(datos))

    """
    miCursor.execute(
         "INSERT INTO DATOSUSUARIOS VALUES(NULL, '" + miNombre.get() +
         "','" + miApellido.get() +
         "','" + miPass.get() +
         "','" + miDireccion.get() +
         "','" + textoComentario.get("1.0", END) +  "')")
    """
    miConexion.commit()
    messagebox.showinfo("BBDD", "registro insertado con exito")

def leer():
    miConexion=sqlite3.connect("59__BBDD_CRUD_usuario")
    miCursor=miConexion.cursor()
    miCursor.execute("SELECT * FROM DATOSUSUARIOS WHERE ID=" + miId.get())

    elUsuario=miCursor.fetchall() #devuelve un array con todo los registros desde el Select
    #recorrer el array
    for usuario in elUsuario:
        miId.set(usuario[0])
        miNombre.set(usuario[1])
        miApellido.set(usuario[2])
        miPass.set(usuario[3])
        miDireccion.set(usuario[4])
        textoComentario.insert(1.0, usuario[5]) #q'ins desde el 1er caracter el dato usuario[5]
    
    miConexion.commit()

def actualizar():
    ##otro codigo con ?,?,?,? consultas parametrizadas
    miConexion=sqlite3.connect("59__BBDD_CRUD_usuario")
    miCursor=miConexion.cursor()
    try:
        variable_entrada = (miNombre.get(),miApellido.get(), miPass.get(), miDireccion.get(), textoComentario.get('1.0', END), miId.get())
        miCursor.execute(
            "UPDATE DATOSUSUARIOS SET NOM_USUARIO= ?, apellido= ?, password =?, direccion=?, comentarios=? WHERE id= ?", variable_entrada)
        miConexion.commit()
        messagebox.showinfo("DDBB", "Registro actualizado a la base de datos")
    except:
        messagebox.showwarning("ERROR DDBB", "no se actualizo a la base de datos")

    # miConexion=sqlite3.connect("59__BBDD_CRUD_usuario")
    # miCursor=miConexion.cursor()
    # miCursor.execute(
    #      "UPDATE DATOSUSUARIOS SET NOM_USUARIO='" + miNombre.get() +
    #      "', APELLIDO='" + miApellido.get() +
    #      "', PASSWORD='" + miPass.get() +
    #      "', DIRECCION='" + miDireccion.get() +
    #      "', COMENTARIOS='" + textoComentario.get("1.0", END) +
    #      "' WHERE ID=" + miId.get())
    # miConexion.commit()
    # messagebox.showinfo("BBDD", "registro actualizado con exito")

def eliminar():
    miConexion=sqlite3.connect("59__BBDD_CRUD_usuario")
    miCursor=miConexion.cursor()
    miCursor.execute("DELETE FROM DATOSUSUARIOS WHERE ID=" + miId.get())
    miConexion.commit()
    messagebox.showinfo("BBDD", "Registro eliminado con exito")

root=Tk() 

###----------------- 2. FRAMES  ---------------------------------------------
#### 2.1. crear menu

barraMenu = Menu(root) 
root.config(menu=barraMenu, width=300, height=300) 

bbddMenu=Menu(barraMenu, tearoff=0)
bbddMenu.add_command(label="Conectar", command=conexionBBDD)
bbddMenu.add_command(label="Salir", command=salirAplicacion)

borrarMenu=Menu(barraMenu, tearoff=0)
borrarMenu.add_command(label="Limpiar campos", command=limpiarCampos)

crudMenu=Menu(barraMenu, tearoff=0)
crudMenu.add_command(label="Crear", command=crear)
crudMenu.add_command(label="Leer", command=leer)
crudMenu.add_command(label="Actualizar", command=actualizar)
crudMenu.add_command(label="Borrar", command=eliminar)

ayudaMenu=Menu(barraMenu, tearoff=0)
ayudaMenu.add_command(label="Licencia")
ayudaMenu.add_command(label="Acerca de ...")

#agregar al Menu
barraMenu.add_cascade(label="BBDD", menu=bbddMenu)
barraMenu.add_cascade(label="Borrar", menu=borrarMenu)
barraMenu.add_cascade(label="CRUD", menu=crudMenu)
barraMenu.add_cascade(label="Ayuda", menu=ayudaMenu)


#### 2.2. crear campos (input|btons)

miFrame=Frame(root)
miFrame.pack()

miId=StringVar()
miNombre=StringVar()
miApellido=StringVar()
miPass=StringVar()
miDireccion=StringVar()


cuadroID=Entry(miFrame, textvariable=miId)
cuadroID.grid(row=0, column=1, padx=10, pady=10)

cuadroNombre=Entry(miFrame, textvariable=miNombre)
cuadroNombre.grid(row=1, column=1, padx=10, pady=10)
cuadroNombre.config(fg="red", justify="left")

cuadroApellido=Entry(miFrame, textvariable=miApellido)
cuadroApellido.grid(row=2, column=1, padx=10, pady=10)

cuadroPass=Entry(miFrame, textvariable=miPass)
cuadroPass.grid(row=3, column=1, padx=10, pady=10)
cuadroPass.config(show="*")

cuadroDireccion=Entry(miFrame, textvariable=miDireccion)
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

labelApellido=Label(miFrame, text="Apellido:")
labelApellido.grid(row=2, column=0, sticky="e", padx=10, pady=10)

labelPass=Label(miFrame, text="Password:")
labelPass.grid(row=3, column=0, sticky="e",  padx=10, pady=10)

labelDireccion=Label(miFrame, text="Direccion:")
labelDireccion.grid(row=4, column=0, sticky="e",  padx=10, pady=10)

labelComentario=Label(miFrame, text="Comentarios:")
labelComentario.grid(row=5, column=0, sticky="e", padx=10, pady=10)


###----------------- 4. añadir frame botones -------------------------------

miFrame2=Frame(root)
miFrame2.pack()

botonCrear=Button(miFrame2, text="Create", command=crear)
botonCrear.grid(row=1, column=0, sticky="e", padx=10, pady=10)

botonLeer=Button(miFrame2, text="Read", command=leer)
botonLeer.grid(row=1, column=1, sticky="e", padx=10, pady=10)

botonActualizar=Button(miFrame2, text="Update", command=actualizar)
botonActualizar.grid(row=1, column=2, sticky="e", padx=10, pady=10)

botonBorrar=Button(miFrame2, text="Delete", command=eliminar)
botonBorrar.grid(row=1, column=3, sticky="e", padx=10, pady=10)


###----------------- nn -------------------------------



root.mainloop()