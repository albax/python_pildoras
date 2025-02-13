
### BUCLES IV (video 17)
# While
#---------------------------------

# # 1. inicializacion
# i = 1

# # 2. while condicion
# while i < 10:
#     print("nro: " + str(i))
#     i += 1  #i=i+1

# print("termino")    

# #---------------------------------


# edad = int(input("Introduce una edad: "))

# while edad < 5 or edad > 100:
#     print("Has introducido una edad incorrecta. Vuelve a intertarlo")
#     edad = int(input("Introduce tu edad por favor: "))
    
# print("Gracias por colaborar. PASAS")
# print("Edad del aspirante: " + str(edad))

#---------------------------------



import math


print("Programa RAIZ CUADRADA")
nro = int(input("Untroduce un nro: "))

intentos = 0 #contador

while nro < 0:
    print("No se puede")
    
    if intentos == 2:
        print("Intentos superado")
        break
    
    nro = int(input("Introduce un nro: "))
    if nro < 0:
        intentos = intentos + 1

if intentos < 2:
    solucion = math.sqrt(nro)
    print("La raiz cuadrada de: " + str(nro) + " es " + str(solucion))