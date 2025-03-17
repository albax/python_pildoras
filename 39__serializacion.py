###############################################
### SERIALIZACION :: 39__serializacion.py
### SERIALIZACION collecciones
### pickle.dump
###############################################

#---------------------------------

import pickle

list_nombre=["Pedro", "Ana", "Maria", "Isable"]
fichero_binario = open("lista_nombres", "wb")  #abre una lista
pickle.dump(list_nombre, fichero_binario)  #vuelca la lista en fichero
fichero_binario.close()
del(fichero_binario)  #borra el fichero
