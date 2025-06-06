###############################################
### 55__BBDD_I.py
###
### LISTA []
### TUPLA ()
###############################################

##from tkinter import filedialog

import sqlite3

##PASOS##
#1. abrir|crear conexion
miConexion=sqlite3.connect("55__BBDD")

#2. crear puntero - cursor
miCursor=miConexion.cursor()

#3. executar query SQL
# miCursor.lexecute("CREATE TABLE PRODUCTOS(NOMBRE_ARTICULO varchar(50), PRECIO integer, SECCION varchar(20))")

#miCursor.execute("INSERT INTO PRODUCTOS VALUES('balon', 16, 'Deportes')")
##INGRESAR DATOS A TABLA##
'''
    variosProducto = [ #lista
        ("Camiseta", 10, "Deportes"), #tuplas
        ("Jarron", 90, "Ceramica"),
        ("Camion", 20, "Juegueteria"),
        ("tshirt", 40, "Deportes"),
        ("Xiomi m2", 10, "Mobile"),

    miCursor.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?)", variosProducto)
    ]
'''
##RECUPERAR DATOS DE TABLA##
miCursor.execute("SELECT * FROM PRODUCTOS")
variosProductos = miCursor.fetchall()

# print(variosProductos)

for producto in variosProductos:
    # print(producto)
    # print(producto[0])
    print("Nom.Articulo: ", producto[0], " | ", "Precio: ", producto[1])


miConexion.commit()

#5. cerrar conexion
miConexion.close()