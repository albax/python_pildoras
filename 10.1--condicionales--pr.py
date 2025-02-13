
# edad_alumno = int(input("ingresa tu edad: "))

# if edad_alumno > 18:
#     print("Mayor")
# else:
#     print("Menor")
    
#-----------------------------------------

# print("verificacion de acceso")    
# nota_alumno = int(input("Ingrese su nota: "))

# if nota_alumno < 5:
#     print("Insuficiente")

# elif nota_alumno < 6:
#     print("suficiente")

# elif nota_alumno < 7:
#     print("Bien")

# elif nota_alumno < 8:
#     print("Notable")
# else:
#     print("Sobresaliente")


#-----------------------------------------

edad = 99
if 0 < edad < 100:   #1ero evalua 0<edad y luego edad<100
    print("Edad es correcto")
else:
    print("Edad incorrecta")    

#-----------------------------------------    
    
salario_presidente=int(input("Ingrese salario presidente: "))
print("Salario presidente: " + str(salario_presidente))

salario_director=int(input("Ingrese salario director: "))
print("Salario director: " + str(salario_director))

salario_jefe_area=int(input("Ingrese salario Jefe Area: "))
print("Salario jefe_area: " + str(salario_jefe_area))

salario_administrativo=int(input("Ingrese salario presindente: "))
print("Salario administrativo: " + str(salario_administrativo))

if salario_administrativo < salario_jefe_area < salario_director < salario_director:
    print("Todo OK")
else:
    print("Algo Falla")
    


#-----------------------------------------    

# 3 condiciones
print("PROGRAMA DE BECAS 2024")

distancia_escuela = int(input("Introduce la distancia a la escuela en Km: "))
print(distancia_escuela)

nro_hermanos = int(input("Introduce nro de hermanos: "))
print(nro_hermanos)

salario_familiar = int(input("Introduce salario bruto anual: "))
print(salario_familiar)

if distancia_escuela > 40 and nro_hermanos > 2 and salario_familiar <=20000:
    print("APROBADO para BECA")
else:
    print("NO derecho a BECA")    