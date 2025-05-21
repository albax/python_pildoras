###############################################
### 45__GUI_interfaces_IV.py
###
### LISTA []
### TUPLA ()
###############################################


import pickle

class Persona:
    def __init__(self, nombre, genero, edad):
        self.nombre = nombre
        self.genero = genero
        self.edad = edad
        print("Se ha creado una persona nueva con el nombre de ", self.nombre)
        
    def __str__(self):
        return "{} {} {}".format(self.nombre, self.genero, self.edad)
    
class ListaPersonas:
    personas = []
    
    def agregarPersonas(self, p):
        self.personas.append(p)
    
    def mostrarPersonas(self):
        for p in self.personas:
            print(p)

miLista = ListaPersonas()

p = Persona("Sandra", "Femenino", 24)
miLista.agregarPersonas(p)
p = Persona("Anonio", "Masculino", 56)
miLista.agregarPersonas(p)
p = Persona("Ana", "Femenino", 21)
miLista.agregarPersonas(p)

miLista.mostrarPersonas()