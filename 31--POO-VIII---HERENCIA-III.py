###############################################
### POO VIII  HERENCIA.3
###############################################
#---------------------------------
#

class Persona():
    
    # metodo constructor
    def __init__(self, nombre, edad, lugar_residencia):
        self.nombre = nombre
        self.edad = edad
        self.lugar_residencia = lugar_residencia
    
    # metodo
    def descripcion(self):
        print("Nombre: ", self.nombre,
              "\nEdad: ", self.edad,
              "\nResidencia: ", self.lugar_residencia)

# HERENCIA
class Empleado(Persona):
    def __init__(self, salario, antiguedad):
        self.salario = salario
        self.antiguedad = antiguedad

    # metodo
    def descripcion(self):
        print("Salario: ", self.salario,
              "\nAntiguedad: ", self.antiguedad)


# Instancia
Antonio = Persona("Antonio", 55, "España")
Antonio.descripcion()

Burse = Empleado("Burse", 32, "Argentina", 2000, "3 años")
Burse.descripcion()