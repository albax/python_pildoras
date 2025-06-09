###############################################
### 58_1__BBDD_IV_CRUD.py
###
### LISTA []
### TUPLA ()
###############################################

import sqlite3

##PASOS##
#1. abrir|crear conexion
##gestionProductos
miConexion=sqlite3.connect("58_1__BBDD_IV_CRUD")

#2. crear puntero - cursor
miCursor=miConexion.cursor()

#3. executar query SQL
#### CRUD ####
#### 1. CREATE ####
# miCursor.execute('''
#     CREATE TABLE PRODUCTOS(
#         ID INTEGER PRIMARY KEY AUTOINCREMENT,
#         NOM_ARTICULO VARCHAR(50) UNIQUE,
#         PRECIO INTEGER,
#         SECCION VARCHAR(20)
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
miCursor.execute("SELECT * FROM PRODUCTOS WHERE SECCION='jugueteria'")
productos=miCursor.fetchall()
print(productos)

#### UPDATE ####
##"SET PRECIO=366"
miCursor.execute("UPDATE PRODUCTOS SET PRECIO=366 WHERE NOM_ARTICULO='pelota'")

#### DELETE ####
##"DELETE FROM PRODUCTOS WHERE ID=5"
miCursor.execute("DELETE FROM PRODUCTOS WHERE ID=5")


miConexion.commit()

#5. cerrar conexion
miConexion.close()