
### BUCLES IV (video 18)
# continue pass else
#---------------------------------

# nombre = input("Ingrese su Nombre: ")
# print(type(nombre))

# for i in nombre:
#     print(i)

# #---------------------------------

# nombre_curso = input("Ingrese su Curso: ")
# print("hay: " + str(len(nombre_curso)))
# contador = 0   #

# for i in nombre_curso:
#     print(i)
#     if i == " ": #verfica espacio en blanco
#         continue
#     contador += 1  #contador = contador + 1
    
# print("hay sin espacios: " + (str(contador))) #da la cant sin espacio


#---------------------------------

email = input("Ingrese su email: ")

for i in email:
    if i =="@":
        arroba = True
        break
else:
    arroba = False
print(arroba)