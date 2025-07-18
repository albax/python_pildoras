###############################################
### 67_1__filter-lambda_EX.py
###
### LISTA []
### TUPLA ()
###############################################


class Empleado:
    def __init__(self, nombre, cargo, salario):
        self.nombre = nombre
        self.cargo = cargo
        self.salario = salario

    def __str__(self):
        return "{} trabaja como {} tiene un saalrio de S{}.". format(self.nombre, self.cargo, self.salario)
    

listaEmpleados = [
    Empleado("Juan", "Director", 14000),
    Empleado("Ana", "subDirector", 9000),
    Empleado("Pedro", "Gerente Ventas", 8000),
    Empleado("Lola", "Gerente Personal", 9500),
    Empleado("Kiko", "Bufon", 4000),
    Empleado("Lony", "Secretaria", 1400),
]

salarios_altos=filter(lambda empleado:empleado.salario>1000, listaEmpleados)

## hya q iterarlos
for empleado_salario in salarios_altos:
    print(empleado_salario)