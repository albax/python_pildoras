###############################################
### 41Cn__getattr_Atributos.py
###
### LISTA []
### TUPLA ()
###############################################


class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

persona = Persona("María", 30)

# Lista de atributos a buscar
atributos = ['nombre', 'edad', 'telefono']

for attr in atributos:
    valor = getattr(persona, attr, 'No disponible')
    print(f"{attr}: {valor}")