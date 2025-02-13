
### CONDICIONALES

#---------------------------------

# def evaluacion(nota):
#     if nota > 10:
#         print("Aprobado")
#     else:
#         print("Desaprobado")

#---------------------------------

print("Dashboard")
nota_alumno = input("Ingrese su nota: ")

def evaluacion2(nota):
    valora_nota = "Aprobado"
    if nota < 5:
        valora_nota = "ReBrutooo"
    return valora_nota

# evaluacion(11)
print(evaluacion2(int(nota_alumno)))


# ELIF
#-----------------------------------------

print("verificacion de acceso")    
nota_alumno = int(input("Ingrese su nota: "))

if nota_alumno < 5:
    print("Insuficiente")

elif nota_alumno < 6:
    print("suficiente")

elif nota_alumno < 7:
    print("Bien")

elif nota_alumno < 8:
    print("Notable")
else:
    print("Sobresaliente")


# CONCANETACION DE OPERADORES
#-----------------------------------------    

edad = 99
if 0 < edad < 100:   #1ero evalua 0<edad y luego edad<100
    print("Edad es correcto")
else:
    print("Edad incorrecta")    