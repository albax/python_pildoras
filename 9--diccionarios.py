
### DICCIONARIOS {} | {()} | dict( ) | dict([ () ])  ||| clave:valor
### TUPLA ()
### LISTA [] -- array

import os

midiccionario0 = {("Jun",8.9,True,"Olivera", 2012)}
print(type(midiccionario0))  # <class 'set'>
print(midiccionario0)  # {('Jun', 8.9, True, 'Olivera', 2012)}


midicc = {"Alemania":"Berlin", "Francia":"Paris", "Reino Unido":"Londres", "España":"Madrid"}
print(midicc)  # imprime todo
print(midicc["Francia"]) # Paris

#add
midicc["Italia"] = "Roma"
print(midicc)  # imprime todo

#del
del midicc["Reino Unido"]
print(midicc)  # imprime todo

midicc2 = {"Alemania":"Berlin", 23:"Jordan", "Mosqueteros":3}
print(midicc2)

# de una LISTA|TUPLA hasta un diccionario
print('MITUPLA-------------------------')
mitupla = ["España", "Francia", "Reino Unido"]
midiccionario1={mitupla[0]:"Madrid",mitupla[1]:"Paris",mitupla[2]:"Londres"}
print(type(mitupla)) # <class 'list'>
print(type(midiccionario1)) # <class 'dict'>
print(midiccionario1["Francia"])
print(midiccionario1)  # imprimir todo :: {'España': 'Madrid', 'Francia': 'Paris', 'Reino Unido': 'Londres'}


# ------------------------------------------------------------------------

print('-------------------------')
# LISTA dentro de un diccionario
midicc3 = {23:"Jordan", "Nombre":"Michael", "Equipo":"Chicago Bulls", "anillos":[1991,1992,1993,1996,1997,1998]}
print(type(midicc3["anillos"])) # <class 'list'>  |  [1991, 1992, 1993, 1996, 1997, 1998] 
result = (midicc3["anillos"]) # [1991, 1992, 1993, 1996, 1997, 1998]
print("LISTA: " + str(result))
print('-------------------------')

# TUPLA dentro de un diccionario
midicc3 = {23:"Jordan", "Nombre":"Michael", "Equipo":"Chicago Bulls", "anillos":(1991,1992,1993,1996,1997,1998)}
print(type(midicc3)) # <class 'dict'>
print(type(midicc3["anillos"])) # <class 'tuple'> |  (1991, 1992, 1993, 1996, 1997, 1998)
result = (midicc3["anillos"]) # [1991, 1992, 1993, 1996, 1997, 1998]
print("TUPLA: " + str(result))

print('-------------------------')
# DICCT dentro de un diccionario
midicc3a = {23:"Jordan", "Nombre":"Michael", "Equipo":"Chicago Bulls", "anillos":{1991,1992,1993,1996,1997,1998}}
midicc3b = {23:"Jordan", "Nombre":"Michael", "Equipo":"Chicago Bulls", "anillos":{"temporadas":[1991,1992,1993,1996,1997,1998]}}
print(type(midicc3a)) # <class 'dict'>
print(type(midicc3b)) # <class 'dict'>
print(type(midicc3b["anillos"]["temporadas"])) # <class 'list'>
result = (midicc3b["anillos"]) 
print("DICCT: " + str(result))  # DICCT: {'temporadas': [1991, 1992, 1993, 1996, 1997, 1998]}

print(midicc3b)  # {23: 'Jordan', 'Nombre': 'Michael', 'Equipo': 'Chicago Bulls', 'anillos': {'temporadas': [1991, 1992, 1993, 1996, 1997, 1998]}}


# ------------------------------------------------------------------------

# METODOS de un diccionario
midicc3c = {23:"Jordan", "Nombre":"Michael", "Equipo":"Chicago Bulls", "anillos":{"temporadas":[1991,1992,1993,1996,1997,1998]}}
print(midicc3c.keys)
print(midicc3c)


# ------------------------------------------------------------------------

#Para Unix/Linux/MacOS/BSD
# os.system ("clear") 
 
#Para DOS/Windows
os.system ("cls") 

# ------------------------------------------------------------------------

# Iterar diccionario
print('-------------------------')
# key
for x in midicc3b:
    print(x)

print('-------------------------')

# values
for x in midicc3b:
    print(midicc3b[x])    

print('-------------------------')

# keys y values    
for x, y in midicc3b.items():
    print(x, y)    

print('# ------------------------------------------------------------------------')

## METODOS
# get

print(midicc3b.get('Jordan')) #1
print(midicc3b.get('Jordan', 'No encontrado'))    