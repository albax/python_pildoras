# METODOS de un diccionario
midicc3c = {23:"Jordan", "Nombre":"Michael", "Equipo":"Chicago Bulls", "anillos":{"temporadas":[1991,1992,1993,1996,1997,1998]}}

#Keys
print(midicc3c.keys())
# print(midicc3c) # dict_keys([23, 'Nombre', 'Equipo', 'anillos'])

#Values
print(midicc3c.values())
# [*midicc3c.values()]
# list(midicc3c.values())

print(type(midicc3c.values())) #<class 'dict_values'>
print(type([*midicc3c.values()])) #<class 'list'> :: otraForma
print(type(list(midicc3c.values()))) #<class 'list'> :: otraForma
# print(midicc3c) # dict_values(['Jordan', 'Michael', 'Chicago Bulls', {'temporadas': [1991, 1992, 1993, 1996, 1997, 1998]}])

#Busca elem, si no encuentra devuelve msj
# print(midicc3c.get("Equipo",'No se encuentra')) #Chicago Bulls

#genera LISTA clave:valor
# print(midicc3c.items()) #dict_items([(23, 'Jordan'), ('Nombre', 'Michael'), ('Equipo', 'Chicago Bulls'), ('anillos', {'temporadas': [1991, 1992, 1993, 1996, 1997, 1998]})])

#extrae y borra registro, devuelve msj
# print(midicc3c.pop("Equipo1","No se ha encontrado"))

#borrar todos los registros
# print(midicc3c.clear()) # None
print(midicc3c) # {}


print("----------------------")
# enum
for clave, valor in midicc3c.items():
    print(clave,":",valor)
    

## [https://docs.hektorprofe.net/python/metodos-de-las-colecciones/metodos-de-los-diccionarios/ ]