###############################################
### SERIALIZACION :: 39.1__serializacion.py
### SERIALIZACION collecciones
### pickle.load
###############################################

#---------------------------------

import pickle

fichero = open("lista_nombres", "rb")  #abre una lista r(lectura)
lista = pickle.load(fichero)  #carga todo lo volcado en lista

print(lista)
