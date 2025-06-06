###############################################
### 57__BBDD_III_primaryKEY.py
###
### LISTA []
### TUPLA ()
###############################################

##from tkinter import filedialog

import sqlite3

##PASOS##
#1. abrir|crear conexion
miConexion=sqlite3.connect("57__BBDD_III_GestionProductos")

#2. crear puntero - cursor
miCursor=miConexion.cursor()

#3. executar query SQL
##INGRESAR DATOS A TABLA##
# miCursor.execute('''
#     CREATE TABLE PRODUCTOS(
#         COD_ARTICULO VARCHAR(4) PRIMARY KEY,
#         NOM_ARTICULO VARCHAR(50),
#         PRECIO INTEGER,
#         SECCION VARCHAR(20)
#     )
# ''')
##RECUPERAR DATOS DE TABLA##
productos = [
    ("AR01", "pelota", 20, "jugueteria"),
    ("AR02", "blusa", 20, "confeccion"),
    ("AR03", "destornillador", 20, "ferreteria"),
    ("AR04", "botya", 20, "ceramica"),
    ("AR05", "superman", 20, "jugueteria"),
    ("AR06", "robot", 20, "robotica")
]

miCursor.executemany("INSERT INTO PRODUCTOS VALUES(?,?,?,?)", productos)
# miCursor.execute("INSERT INTO PRODUCTOS VALUES('AR06','tren', 16, 'Jugueteria')") #sqlite3.IntegrityError: UNIQUE constraint failed: PRODUCTOS.COD_ARTICULO

miConexion.commit()

#5. cerrar conexion
miConexion.close()