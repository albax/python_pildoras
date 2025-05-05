###############################################
### 41B__fstrings-timeit.py
###
### LISTA []
### TUPLA ()
###############################################


import timeit

nombre = "Juan"
edad = 30

#uso f-strings
calc_fstring = timeit.timeit('f"Hola {nombre} tienes {edad} años"', globals = globals(), number = 1000000)

#uso format
calc_format = timeit.timeit('"Hola {} tienes {} años.".format(nombre, edad)', globals=globals(), number=1000000)

print(f"Tiempo fstrings: {calc_fstring} seg") #Tiempo fstrings: 0.18387649999931455 seg
print(f"Tiempo .format(): {calc_format} seg") #Tiempo .format(): 0.4549011000053724 seg

# globals=globals() # acceder a las fn globales
# number=1000000 # exec un millon de veces

print("---------------------------------------------------")

pi = 3.141657
print(f"Valor de PI es {pi:.2f}")
print("Valor de pi es {:.2f}".format(pi))
