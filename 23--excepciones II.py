### excepciones II (video 22 | 23)
# 
#---------------------------------
# except

# def divide():
#     try:
#         op1 = (float(input("Introduce el num1: ")))
#         op2 = (float(input("Introduce el num2: ")))
#         print("La DIV es: " + str(op1/op2))
        
#     except ValueError:
#         print("El valor introducido es erroneo")
    
#     except ZeroDivisionError:
#         print("NO se puede DIVIDOR entre 0! ")
    
#     print("Calculo finalizado")
    
# divide()

# #---------------------------------
# # finally

# def divide():
#     try:
#         op1 = (float(input("Introduce el num1: ")))
#         op2 = (float(input("Introduce el num2: ")))
#         print("La DIV es: " + str(op1/op2))
        
#     # se ejecuta la ult linea
#     finally:
#         print("Calculo finalizado")
    
# divide()

#---------------------------------
# raise

# lanzar nosotros una excepción manualmente, usando raise

edad = int(input("ingrese tu edad: "))
def evaluaEdad(edad):
    
    if edad < 0:
        raise TypeError("No se permiten edades negativas") #personalizar mensaje  | ZeroDivisionError | TypeError | [NameError] myPropioError ... No Definido
    
    if edad < 20:
        return "Eres muy joven"
    elif edad < 40:
        return "Eres joven"
    elif edad < 65:
        return "Eres Maduro"
    elif edad < 100:
        return "La tierra te llama ... "
    else:
        print("Considerate difunto")
    
print(evaluaEdad(edad))
        
        
#---------------------------------
# import math
# math.sqrt        

import math
def calculRaiz(num1):
    
    if num1 < 0:
        raise ValueError("El nro no puede ser NEGATIVO")
    else:
        return math.sqrt(num1)

op1 = (int(input("Introduce un nro: ")))

try:
    raiz = calculRaiz(op1)
    print("SQRT: " + str(raiz))
except ValueError as ErrorDeNumeroNegativo: #esta conectado con el raise
    print(ErrorDeNumeroNegativo)
    
print("Programa terminado")