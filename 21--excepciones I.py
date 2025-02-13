### excepciones I (video 21)
# 
#---------------------------------

def suma(num1, num2):
    return num1 + num2

def resta(num1, num2):
    return num1 - num2

def multiplica(num1, num2):
    return num1 * num2

def divide(num1, num2):
    try:
        return num1 / num2
    
    except ZeroDivisionError:
        print("No se puede dividir")
        return "Operacion ERRONEA" #si no hay return devuelve NONE

#bucle bucle
while True: #bucle infinito, con break sale INTERESANTE
    try:
        op1 = (int(input("Introduce num1: ")))
        op2 = (int(input("Introduce num2: ")))
        break #si los 2 arriba son correctos, leeara el break, sin pasar por el except
    
    except ValueError:
        print("Los valores introducidos no son correctos. Intenta nuevamente")    
    

operacion = input("Introduce la operacion (suma, resta, multiplica, divide): ")

if operacion == "suma":
    print(suma(op1,op2))
    
elif operacion == "resta":
    print(resta(op1,op2))
    
elif operacion == "multiplica":
    print(multiplica(op1,op2))
    
elif operacion == "divide":
    print(divide(op1,op2))

else:
    print("Operacion NO COMPLETADA") 

print("Operacion EJECUTADA. continuacion")