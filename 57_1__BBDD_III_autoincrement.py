###############################################
### 57_1__BBDD_III_autoincrement.py
###
### LISTA []
### TUPLA ()
###############################################

import sqlite3

##PASOS##
#1. abrir|crear conexion
miConexion=sqlite3.connect("57_1__BBDD_III_autoincrement")

#2. crear puntero - cursor
miCursor=miConexion.cursor()

#3. executar query SQL
##INGRESAR DATOS A TABLA##
miCursor.execute('''
    CREATE TABLE PRODUCTOS(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        NOM_ARTICULO VARCHAR(50),
        PRECIO INTEGER,
        SECCION VARCHAR(20)
    )
''')
##RECUPERAR DATOS DE TABLA##
productos = [
    ("pelota", 20, "jugueteria"),
    ("blusa", 10, "confeccion"),
    ("destornillador", 40, "ferreteria"),
    ("botya", 120, "ceramica"),
    ("superman", 90, "jugueteria"),
    ("robot", 50, "robotica")
]

miCursor.executemany("INSERT INTO PRODUCTOS VALUES(NULL,?,?,?)", productos)

miConexion.commit()

#5. cerrar conexion
miConexion.close()